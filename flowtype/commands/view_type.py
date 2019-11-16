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

            # Fix problem with < and >
            formattedString = stdout["type"].replace("<", lt).replace(">", gt)
            logger.logger.info(formattedString)

            # ADD BR
            # Add new lines for curly
            formattedString = re.sub(
                r"{(.+)}", leftCurly + br + r"\1" + br + rightCurly, formattedString
            )

            # Add new lines for braces
            formattedString = re.sub(
                r"\((.+?)\)", leftBrace + br + r"\1" + br + rightBrace, formattedString
            )

            # Add new lines for commas
            formattedString = re.sub(
                r"(,) ([a-zA-Z?]+:?)", r"\1<br>\2", formattedString
            )

            # FORMAT lines
            formattedString = formattedString.split(br)

            resultString = ""
            level = 0
            for line in formattedString:
                if rightCurly in line or rightBrace in line:
                    level = level - 1
                resultString = (
                    resultString + ("&nbsp;&nbsp;" * level) + line.strip() + br
                )
                if leftCurly in line or leftBrace in line:
                    level = level + 1

            self.view.show_popup(
                """<html><body><p>""" + resultString + """</p></body></html>""",
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
