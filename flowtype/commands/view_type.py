import re
from .base import BaseCommand
from .exec_flow import ExecFlowCommand
from ..logger import Logger
from ..helpers import prepare_arguments

logger = Logger()


class FlowtypeViewType(BaseCommand):
    """Run Flow type-at-pos and popup type definition."""

    def get_cmd(self):
        """Construct cli command."""
        try:
            flow_bin = self.get_flow_bin()
            logger.logger.debug("using flow-bin %s" % flow_bin)
        except ValueError as e:
            logger.logger.error("type-at-pos %s" % e)
            return

        try:
            project_root = self.get_project_root()
        except ValueError as e:
            logger.logger.error("type-at-pos %s" % e)
            return

        arguments = prepare_arguments(self.view)

        cmd = [
            flow_bin,
            "type-at-pos",
            "--from",
            "nuclide",
            # "--expand-json-output",
            "--root",
            project_root,
            "--path",
            arguments.file_name,
            "--quiet",
            "--pretty",
            "--json",
            str(arguments.row + 1),
            str(arguments.col + 1),
        ]

        return cmd

    def handle_process(self, returncode, stdout, error):
        """Handle the output from the threaded process."""
        if type(error) is bytes:
            error = error.decode("utf-8")

        if returncode != 0:
            logger.logger.error("type-at-pos %s" % error)
            return

        if stdout:
            leftCurly = "{"
            rightCurly = "}"
            leftBrace = "("
            rightBrace = ")"
            lt = "&lt;"
            gt = "&gt;"
            br = "<br>"
            comma = ","

            # Fix problem with < and >
            formattedString = stdout["type"].replace("<", lt).replace(">", gt)
            logger.logger.info(formattedString)

            # ADD BR
            tempRes = ""
            level = 0
            for char in formattedString:
                if char == leftCurly or char == leftBrace:
                    level = level + 1
                    tempRes = tempRes + char + br + ("&nbsp;&nbsp;" * level)
                elif char == rightCurly or char == rightBrace:
                    level = level - 1
                    tempRes = tempRes + br + ("&nbsp;&nbsp;" * level) + char
                elif char == comma:
                    tempRes = tempRes + char + br + ("&nbsp;&nbsp;" * level)
                elif char == " ":
                    if not tempRes.endswith("&nbsp;"):
                        tempRes = tempRes + char
                else:
                    tempRes = tempRes + char

            formattedString = tempRes
            self.view.show_popup(
                """<html><body><p>""" + formattedString + """</p></body></html>""",
                max_width=800,
                max_height=2400,
            )
        else:
            self.view.set_status("flow_type", "Flow: no type found")

    def run(self, view):
        """Execute `type-at-pos` command."""
        logger.logger.debug("Running type-at-pos")

        self.view.erase_status("flow_type")

        thread = ExecFlowCommand(self.get_cmd(), self.get_content())
        thread.start()
        self.check_thread(thread)
