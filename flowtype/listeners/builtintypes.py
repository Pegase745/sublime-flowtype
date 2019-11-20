"""
Flow's list of built-in types available in 0.44.0 (Apr 13, 2017).

Related to
    https://flow.org/en/docs/types/
and
    http://www.saltycrane.com/blog/2016/06/flow-type-cheat-sheet/
"""


def print_type_format(trigger, content=None, description=None):
    """Format output for autocompletion for a given trigger text."""
    return ("%s\t%s" % (trigger, description), "%s" % (content or trigger))


builtintypes = [
    # Built-in types
    print_type_format("any", description="Flow built-in type"),
    print_type_format("boolean", description="Flow built-in type"),
    print_type_format("null", description="Flow built-in type"),
    print_type_format("number", description="Flow built-in type"),
    print_type_format("mixed", description="Flow built-in type"),
    print_type_format("string", description="Flow built-in type"),
    print_type_format("void", description="Flow built-in type"),
    print_type_format("Class", "Class<${1}>", "Flow built-in type"),
    # Built-in 'private' types
    print_type_format(
        "Abstract", "\$Abstract<${1}>", "Flow built-in private type"
    ),
    print_type_format(
        "Diff", "\$Diff<${1}, ${2}>", "Flow built-in private type"
    ),
    print_type_format("Exact", "\$Exact<${1}>", "Flow built-in private type"),
    print_type_format("Keys", "\$Keys<${1}>", "Flow built-in private type"),
    print_type_format(
        "ObjMap", "\$ObjMap<${1}, ${2}>", "Flow built-in private type"
    ),
    print_type_format(
        "PropertyType",
        "\$PropertyType<${1}, ${2}>",
        "Flow built-in private type",
    ),
    print_type_format(
        "Subtype", "\$Subtype<${1}, ${2}>", "Flow built-in private type"
    ),
    print_type_format(
        "Supertype", "\$Supertype<${1}, ${2}>", "Flow built-in private type"
    ),
    # Core types
    print_type_format("Array", "Array<${1}>", "Flow core type"),
    print_type_format("ArrayBuffer", description="Flow core type"),
    print_type_format(
        "AsyncIterable", "AsyncIterable<${1}>", "Flow core type"
    ),
    print_type_format(
        "AsyncIterator", "AsyncIterator<${1}>", "Flow core type"
    ),
    print_type_format("Boolean", description="Flow core type"),
    print_type_format("CallSite", description="Flow core type"),
    print_type_format("DataView", description="Flow core type"),
    print_type_format("Date", description="Flow core type"),
    print_type_format("Error", description="Flow core type"),
    print_type_format("EvalError", description="Flow core type"),
    print_type_format("Float32Array", description="Flow core type"),
    print_type_format("Float64Array", description="Flow core type"),
    print_type_format("Function", description="Flow core type"),
    print_type_format("global", description="Flow core type"),
    print_type_format("Infinity", description="Flow core type"),
    print_type_format("Int16Array", description="Flow core type"),
    print_type_format("Int32Array", description="Flow core type"),
    print_type_format("Int8Array", description="Flow core type"),
    print_type_format("Iterable", "Iterable<${1}>", "Flow core type"),
    print_type_format("Iterator", "Iterator<${1}>", "Flow core type"),
    print_type_format(
        "IteratorResult", "IteratorResult<${1}, ${2}>", "Flow core type"
    ),
    print_type_format("JSON", description="Flow core type"),
    print_type_format("Map", "Map<${1}, ${2}>", "Flow core type"),
    print_type_format("NaN", description="Flow core type"),
    print_type_format("Number", description="Flow core type"),
    print_type_format("Object", description="Flow core type"),
    print_type_format("Promise", "Promise<${1}>", "Flow core type"),
    print_type_format("Proxy", "Proxy<${1}>", "Flow core type"),
    print_type_format("RangeError", description="Flow core type"),
    print_type_format("ReferenceError", description="Flow core type"),
    print_type_format("Reflect", description="Flow core type"),
    print_type_format("RegExp", description="Flow core type"),
    print_type_format("Set", "Set<${1}>", "Flow core type"),
    print_type_format("String", description="Flow core type"),
    print_type_format("Symbol", description="Flow core type"),
    print_type_format("SyntaxError", description="Flow core type"),
    print_type_format("TypeError", description="Flow core type"),
    print_type_format("Uint16Array", description="Flow core type"),
    print_type_format("Uint32Array", description="Flow core type"),
    print_type_format("Uint8Array", description="Flow core type"),
    print_type_format("Uint8ClampedArray", description="Flow core type"),
    print_type_format("URIError", description="Flow core type"),
    print_type_format("WeakMap", "WeakMap<${1}, ${2}>", "Flow core type"),
    print_type_format("WeakSet", "WeakSet<${1}>", "Flow core type"),
    # Core 'private' types
    print_type_format(
        "ArrayBufferView",
        "\$ArrayBufferView",
        description="Flow core private type",
    ),
    print_type_format(
        "ReadOnlyArray",
        "\$ReadOnlyArray<${1}>",
        description="Flow core private type",
    ),
    print_type_format(
        "SymboIsConcatSpreadable",
        "\$SymboIsConcatSpreadable",
        description="Flow core private type",
    ),
    print_type_format(
        "SymbolHasInstance",
        "\$SymbolHasInstance",
        description="Flow core private type",
    ),
    print_type_format(
        "SymbolIterator",
        "\$SymbolIterator",
        description="Flow core private type",
    ),
    print_type_format(
        "SymbolMatch", "\$SymbolMatch", description="Flow core private type"
    ),
    print_type_format(
        "SymbolReplace",
        "\$SymbolReplace",
        description="Flow core private type",
    ),
    print_type_format(
        "SymbolSearch", "\$SymbolSearch", description="Flow core private type"
    ),
    print_type_format(
        "SymbolSpecies",
        "\$SymbolSpecies",
        description="Flow core private type",
    ),
    print_type_format(
        "SymbolSplit", "\$SymbolSplit", description="Flow core private type"
    ),
    print_type_format(
        "SymbolToPrimitive",
        "\$SymbolToPrimitive",
        description="Flow core private type",
    ),
    print_type_format(
        "SymbolToStringTag",
        "\$SymbolToStringTag",
        description="Flow core private type",
    ),
    print_type_format(
        "SymbolUnscopables",
        "\$SymbolUnscopables",
        description="Flow core private type",
    ),
    print_type_format(
        "TypedArray", "\$TypedArray", description="Flow core private type"
    ),
    print_type_format(
        "Proxyrevocable",
        "Proxy\$revocable<${1}>",
        description="Flow core private type",
    ),
    print_type_format(
        "Proxytraps",
        "Proxy\$traps<${1}>",
        description="Flow core private type",
    ),
    print_type_format(
        "RegExpflags", "RegExp\$flags", description="Flow core private type"
    ),
    # React types
    print_type_format(
        "_ReactClass", "_ReactClass<${1}, ${2}, ${3}, ${4}>", "Flow React type"
    ),
    print_type_format(
        "LegacyReactComponent",
        "LegacyReactComponent<${1}, ${2}, ${3}>",
        "Flow React type",
    ),
    print_type_format("ReactClass", "ReactClass<${1}>", "Flow React type"),
    print_type_format(
        "ReactPropsChainableTypeChecker", description="Flow React type"
    ),
    print_type_format("ReactPropsCheckType", description="Flow React type"),
    print_type_format("ReactPropTypes", description="Flow React type"),
    print_type_format(
        "SyntheticClipboardEvent", description="Flow React type"
    ),
    print_type_format(
        "SyntheticCompositionEvent", description="Flow React type"
    ),
    print_type_format("SyntheticDragEvent", description="Flow React type"),
    print_type_format("SyntheticEvent", description="Flow React type"),
    print_type_format("SyntheticFocusEvent", description="Flow React type"),
    print_type_format("SyntheticInputEvent", description="Flow React type"),
    print_type_format("SyntheticKeyboardEvent", description="Flow React type"),
    print_type_format("SyntheticMouseEvent", description="Flow React type"),
    print_type_format("SyntheticTouchEvent", description="Flow React type"),
    print_type_format("SyntheticUIEvent", description="Flow React type"),
    print_type_format("SyntheticWheelEvent", description="Flow React type"),
    # React 'private' types
    print_type_format(
        "DefaultPropsOf", "\$DefaultPropsOf<${1}>", "Flow React type"
    ),
    print_type_format("JSXIntrinsics", "\$JSXIntrinsics", "Flow React type"),
    print_type_format("PropsOf", "\$PropsOf<${1}>", "Flow React type"),
    print_type_format(
        "ReactComponent",
        "React\$Component<${1}, ${2}, ${3}>",
        "Flow React type",
    ),
    print_type_format(
        "ReactElement", "React\$Element<${1}>", "Flow React type"
    ),
    print_type_format(
        "ReactPropTypesarrayOf", "React\$PropTypes\$arrayOf", "Flow React type"
    ),
    print_type_format(
        "ReactPropTypesinstanceOf",
        "React\$PropTypes\$instanceOf",
        "Flow React type",
    ),
    print_type_format(
        "ReactPropTypesobjectOf",
        "React\$PropTypes\$objectOf",
        "Flow React type",
    ),
    print_type_format(
        "ReactPropTypesoneOf", "React\$PropTypes\$oneOf", "Flow React type"
    ),
    print_type_format(
        "ReactPropTypesoneOfType",
        "React\$PropTypes\$oneOfType",
        "Flow React type",
    ),
    print_type_format(
        "ReactPropTypesshape", "React\$PropTypes\$shape", "Flow React type"
    ),
    print_type_format(
        "React$PureComponent",
        "React\$PureComponent<${1}, ${2}, ${3}>",
        "Flow React type",
    ),
    # Document Object Model types
    print_type_format("AnimationEvent", description="Flow DOM type"),
    print_type_format("AnimationEventHandler", description="Flow DOM type"),
    print_type_format("AnimationEventListener", description="Flow DOM type"),
    print_type_format("AnimationEventTypes", description="Flow DOM type"),
    print_type_format("Attr", description="Flow DOM type"),
    print_type_format("AudioTrack", description="Flow DOM type"),
    print_type_format("AudioTrackList", description="Flow DOM type"),
    print_type_format("Blob", description="Flow DOM type"),
    print_type_format("BufferDataSource", description="Flow DOM type"),
    print_type_format("CanvasDrawingStyles", description="Flow DOM type"),
    print_type_format("CanvasFillRule", description="Flow DOM type"),
    print_type_format("CanvasGradient", description="Flow DOM type"),
    print_type_format("CanvasImageSource", description="Flow DOM type"),
    print_type_format("CanvasPattern", description="Flow DOM type"),
    print_type_format("CanvasRenderingContext2D", description="Flow DOM type"),
    print_type_format("CharacterData", description="Flow DOM type"),
    print_type_format("ClientRect", description="Flow DOM type"),
    print_type_format("ClientRectList", description="Flow DOM type"),
    print_type_format("Comment", description="Flow DOM type"),
    print_type_format("CustomElementRegistry", description="Flow DOM type"),
    print_type_format("CustomEvent", description="Flow DOM type"),
    print_type_format("DataTransfer", description="Flow DOM type"),
    print_type_format("DataTransferItem", description="Flow DOM type"),
    print_type_format("DataTransferItemList", description="Flow DOM type"),
    print_type_format("Document", description="Flow DOM type"),
    print_type_format("DocumentFragment", description="Flow DOM type"),
    print_type_format("DocumentType", description="Flow DOM type"),
    print_type_format("DOMError", description="Flow DOM type"),
    print_type_format("DOMImplementation", description="Flow DOM type"),
    print_type_format("DOMTokenList", description="Flow DOM type"),
    print_type_format("DragEvent", description="Flow DOM type"),
    print_type_format("DragEventHandler", description="Flow DOM type"),
    print_type_format("DragEventListener", description="Flow DOM type"),
    print_type_format("DragEventTypes", description="Flow DOM type"),
    print_type_format("Element", description="Flow DOM type"),
    print_type_format(
        "ElementRegistrationOptions", description="Flow DOM type"
    ),
    print_type_format("Event", description="Flow DOM type"),
    print_type_format("EventHandler", description="Flow DOM type"),
    print_type_format("EventListener", description="Flow DOM type"),
    print_type_format(
        "EventListenerOptionsOrUseCapture", description="Flow DOM type"
    ),
    print_type_format("EventTarget", description="Flow DOM type"),
    print_type_format("File", description="Flow DOM type"),
    print_type_format("FileList", description="Flow DOM type"),
    print_type_format("FileReader", description="Flow DOM type"),
    print_type_format("HitRegionOptions", description="Flow DOM type"),
    print_type_format("HTMLAnchorElement", description="Flow DOM type"),
    print_type_format("HTMLAppletElement", description="Flow DOM type"),
    print_type_format("HTMLAudioElement", description="Flow DOM type"),
    print_type_format("HTMLBaseElement", description="Flow DOM type"),
    print_type_format("HTMLButtonElement", description="Flow DOM type"),
    print_type_format("HTMLCanvasElement", description="Flow DOM type"),
    print_type_format(
        "HTMLCollection", "HTMLCollection<${1}>", "Flow DOM type"
    ),
    print_type_format("HTMLDivElement", description="Flow DOM type"),
    print_type_format("HTMLElement", description="Flow DOM type"),
    print_type_format("HTMLEmbedElement", description="Flow DOM type"),
    print_type_format("HTMLFormElement", description="Flow DOM type"),
    print_type_format("HTMLIFrameElement", description="Flow DOM type"),
    print_type_format("HTMLImageElement", description="Flow DOM type"),
    print_type_format("HTMLInputElement", description="Flow DOM type"),
    print_type_format("HTMLLabelElement", description="Flow DOM type"),
    print_type_format("HTMLLinkElement", description="Flow DOM type"),
    print_type_format("HTMLMediaElement", description="Flow DOM type"),
    print_type_format("HTMLMenuElement", description="Flow DOM type"),
    print_type_format("HTMLMetaElement", description="Flow DOM type"),
    print_type_format("HTMLOptGroupElement", description="Flow DOM type"),
    print_type_format("HTMLOptionElement", description="Flow DOM type"),
    print_type_format("HTMLOptionsCollection", description="Flow DOM type"),
    print_type_format("HTMLParagraphElement", description="Flow DOM type"),
    print_type_format("HTMLScriptElement", description="Flow DOM type"),
    print_type_format("HTMLSelectElement", description="Flow DOM type"),
    print_type_format("HTMLSlotElement", description="Flow DOM type"),
    print_type_format("HTMLSourceElement", description="Flow DOM type"),
    print_type_format("HTMLSpanElement", description="Flow DOM type"),
    print_type_format("HTMLStyleElement", description="Flow DOM type"),
    print_type_format("HTMLTableCaptionElement", description="Flow DOM type"),
    print_type_format("HTMLTableCellElement", description="Flow DOM type"),
    print_type_format("HTMLTableElement", description="Flow DOM type"),
    print_type_format("HTMLTableRowElement", description="Flow DOM type"),
    print_type_format("HTMLTableSectionElement", description="Flow DOM type"),
    print_type_format("HTMLTemplateElement", description="Flow DOM type"),
    print_type_format("HTMLTextAreaElement", description="Flow DOM type"),
    print_type_format("HTMLVideoElement", description="Flow DOM type"),
    print_type_format("Image", description="Flow DOM type"),
    print_type_format("ImageBitmap", description="Flow DOM type"),
    print_type_format("ImageData", description="Flow DOM type"),
    print_type_format("KeyboardEvent", description="Flow DOM type"),
    print_type_format("KeyboardEventHandler", description="Flow DOM type"),
    print_type_format("KeyboardEventListener", description="Flow DOM type"),
    print_type_format("KeyboardEventTypes", description="Flow DOM type"),
    print_type_format("MediaError", description="Flow DOM type"),
    print_type_format("MediaSource", description="Flow DOM type"),
    print_type_format("MessageEvent", description="Flow DOM type"),
    print_type_format("MouseEvent", description="Flow DOM type"),
    print_type_format("MouseEventHandler", description="Flow DOM type"),
    print_type_format("MouseEventListener", description="Flow DOM type"),
    print_type_format("MouseEventTypes", description="Flow DOM type"),
    print_type_format("NamedNodeMap", description="Flow DOM type"),
    print_type_format("Node", description="Flow DOM type"),
    print_type_format("NodeFilter", description="Flow DOM type"),
    print_type_format("NodeFilterCallback", description="Flow DOM type"),
    print_type_format("NodeFilterInterface", description="Flow DOM type"),
    print_type_format(
        "NodeIterator", "NodeIterator<${1}, ${2}>", "Flow DOM type"
    ),
    print_type_format("NodeList", "NodeList<${1}>", "Flow DOM type"),
    print_type_format("Path2D", description="Flow DOM type"),
    print_type_format("ProgressEvent", description="Flow DOM type"),
    print_type_format("ProgressEventHandler", description="Flow DOM type"),
    print_type_format("ProgressEventListener", description="Flow DOM type"),
    print_type_format("ProgressEventTypes", description="Flow DOM type"),
    print_type_format("PromiseRejectionEvent", description="Flow DOM type"),
    print_type_format("Range", description="Flow DOM type"),
    print_type_format("RenderingContext", description="Flow DOM type"),
    print_type_format("Selection", description="Flow DOM type"),
    print_type_format("SelectionDirection", description="Flow DOM type"),
    print_type_format("SelectionMode", description="Flow DOM type"),
    print_type_format("ShadowRoot", description="Flow DOM type"),
    print_type_format("SourceBuffer", description="Flow DOM type"),
    print_type_format("SourceBufferList", description="Flow DOM type"),
    print_type_format("Storage", description="Flow DOM type"),
    print_type_format("SVGMatrix", description="Flow DOM type"),
    print_type_format("TexImageSource", description="Flow DOM type"),
    print_type_format("Text", description="Flow DOM type"),
    print_type_format("TextMetrics", description="Flow DOM type"),
    print_type_format("TextRange", description="Flow DOM type"),
    print_type_format("TextTrack", description="Flow DOM type"),
    print_type_format("TextTrackCue", description="Flow DOM type"),
    print_type_format("TextTrackCueList", description="Flow DOM type"),
    print_type_format("TextTrackList", description="Flow DOM type"),
    print_type_format("TimeRanges", description="Flow DOM type"),
    print_type_format("Touch", description="Flow DOM type"),
    print_type_format("TouchEvent", description="Flow DOM type"),
    print_type_format("TouchEventHandler", description="Flow DOM type"),
    print_type_format("TouchEventListener", description="Flow DOM type"),
    print_type_format("TouchEventTypes", description="Flow DOM type"),
    print_type_format("TouchList", description="Flow DOM type"),
    print_type_format("TrackDefault", description="Flow DOM type"),
    print_type_format("TrackDefaultList", description="Flow DOM type"),
    print_type_format("TreeWalker", "TreeWalker<${1}, ${2}>", "Flow DOM type"),
    print_type_format("UIEvent", description="Flow DOM type"),
    print_type_format("URL", description="Flow DOM type"),
    print_type_format("ValidityState", description="Flow DOM type"),
    print_type_format("VertexAttribFVSource", description="Flow DOM type"),
    print_type_format("VideoTrack", description="Flow DOM type"),
    print_type_format("VideoTrackList", description="Flow DOM type"),
    print_type_format("WebGLContextAttributes", description="Flow DOM type"),
    print_type_format("WebGLContextEvent", description="Flow DOM type"),
    print_type_format("WebGLRenderingContext", description="Flow DOM type"),
    print_type_format("WheelEvent", description="Flow DOM type"),
    print_type_format("WheelEventHandler", description="Flow DOM type"),
    print_type_format("WheelEventListener", description="Flow DOM type"),
    print_type_format("WheelEventTypes", description="Flow DOM type"),
    # Document Object Model 'private' types
    print_type_format(
        "CustomEventInit", "CustomEvent\$Init", "Flow DOM private type"
    ),
    print_type_format("EventInit", "Event\$Init", "Flow DOM private type"),
    # Browser Object Model types
    print_type_format("AnalyserNode", description="Flow BOM type"),
    print_type_format("AudioBuffer", description="Flow BOM type"),
    print_type_format("AudioBufferSourceNode", description="Flow BOM type"),
    print_type_format("AudioContext", description="Flow BOM type"),
    print_type_format("AudioDestinationNode", description="Flow BOM type"),
    print_type_format("AudioListener", description="Flow BOM type"),
    print_type_format("AudioNode", description="Flow BOM type"),
    print_type_format("AudioParam", description="Flow BOM type"),
    print_type_format("BatteryManager", description="Flow BOM type"),
    print_type_format("BiquadFilterNode", description="Flow BOM type"),
    print_type_format("BodyInit", description="Flow BOM type"),
    print_type_format("CacheType", description="Flow BOM type"),
    print_type_format("ChannelMergerNode", description="Flow BOM type"),
    print_type_format("ChannelSplitterNode", description="Flow BOM type"),
    print_type_format("CloseEvent", description="Flow BOM type"),
    print_type_format("ConvolverNode", description="Flow BOM type"),
    print_type_format("Coordinates", description="Flow BOM type"),
    print_type_format("CredentialsType", description="Flow BOM type"),
    print_type_format(
        "DedicatedWorkerGlobalScope", description="Flow BOM type"
    ),
    print_type_format("DelayNode", description="Flow BOM type"),
    print_type_format("DOMParser", description="Flow BOM type"),
    print_type_format("DynamicsCompressorNode", description="Flow BOM type"),
    print_type_format("FormData", description="Flow BOM type"),
    print_type_format("FormDataEntryValue", description="Flow BOM type"),
    print_type_format("GainNode", description="Flow BOM type"),
    print_type_format("Gamepad", description="Flow BOM type"),
    print_type_format("GamepadButton", description="Flow BOM type"),
    print_type_format("Geolocation", description="Flow BOM type"),
    print_type_format("Headers", description="Flow BOM type"),
    print_type_format("HeadersInit", description="Flow BOM type"),
    print_type_format("History", description="Flow BOM type"),
    print_type_format("Location", description="Flow BOM type"),
    print_type_format(
        "MediaElementAudioSourceNode", description="Flow BOM type"
    ),
    print_type_format("MediaStream", description="Flow BOM type"),
    print_type_format(
        "MediaStreamAudioSourceNode", description="Flow BOM type"
    ),
    print_type_format("MediaStreamTrack", description="Flow BOM type"),
    print_type_format("MessageChannel", description="Flow BOM type"),
    print_type_format("MessagePort", description="Flow BOM type"),
    print_type_format("MethodType", description="Flow BOM type"),
    print_type_format("MimeType", description="Flow BOM type"),
    print_type_format("MimeTypeArray", description="Flow BOM type"),
    print_type_format("ModeType", description="Flow BOM type"),
    print_type_format("MutationObserver", description="Flow BOM type"),
    print_type_format(
        "MutationObserverInitRequired", description="Flow BOM type"
    ),
    print_type_format("MutationRecord", description="Flow BOM type"),
    print_type_format("Navigator", description="Flow BOM type"),
    print_type_format("NavigatorCommon", description="Flow BOM type"),
    print_type_format("OscillatorNode", description="Flow BOM type"),
    print_type_format("PannerNode", description="Flow BOM type"),
    print_type_format("Performance", description="Flow BOM type"),
    print_type_format("PerformanceEntry", description="Flow BOM type"),
    print_type_format(
        "PerformanceEntryFilterOptions", description="Flow BOM type"
    ),
    print_type_format("PerformanceNavigation", description="Flow BOM type"),
    print_type_format(
        "PerformanceNavigationTiming", description="Flow BOM type"
    ),
    print_type_format(
        "PerformanceResourceTiming", description="Flow BOM type"
    ),
    print_type_format("PerformanceTiming", description="Flow BOM type"),
    print_type_format("PeriodicWave", description="Flow BOM type"),
    print_type_format("Plugin", description="Flow BOM type"),
    print_type_format("PluginArray", description="Flow BOM type"),
    print_type_format("Position", description="Flow BOM type"),
    print_type_format("PositionError", description="Flow BOM type"),
    print_type_format("PositionOptions", description="Flow BOM type"),
    print_type_format("RedirectType", description="Flow BOM type"),
    print_type_format("ReferrerPolicyType", description="Flow BOM type"),
    print_type_format("Request", description="Flow BOM type"),
    print_type_format("RequestOptions", description="Flow BOM type"),
    print_type_format("Response", description="Flow BOM type"),
    print_type_format("ResponseOptions", description="Flow BOM type"),
    print_type_format("ResponseType", description="Flow BOM type"),
    print_type_format("Screen", description="Flow BOM type"),
    print_type_format("ScriptProcessorNode", description="Flow BOM type"),
    print_type_format("SharedWorker", description="Flow BOM type"),
    print_type_format("SharedWorkerGlobalScope", description="Flow BOM type"),
    print_type_format("TextDecoder", description="Flow BOM type"),
    print_type_format("TextEncoder", description="Flow BOM type"),
    print_type_format("URLSearchParams", description="Flow BOM type"),
    print_type_format("WaveShaperNode", description="Flow BOM type"),
    print_type_format("WebSocket", description="Flow BOM type"),
    print_type_format("Worker", description="Flow BOM type"),
    print_type_format("WorkerGlobalScope", description="Flow BOM type"),
    print_type_format("WorkerLocation", description="Flow BOM type"),
    print_type_format("WorkerNavigator", description="Flow BOM type"),
    print_type_format("XDomainRequest", description="Flow BOM type"),
    print_type_format("XMLHttpRequest", description="Flow BOM type"),
    print_type_format(
        "XMLHttpRequestEventTarget", description="Flow BOM type"
    ),
    print_type_format("XMLSerializer", description="Flow BOM type"),
    # Browser Object Model 'private' types
    print_type_format(
        "TextDecoderavailableEncodings",
        "TextDecoder\$availableEncodings",
        "Flow BOM private type",
    ),
    print_type_format(
        "TextEncoderavailableEncodings",
        "TextEncoder\$availableEncodings",
        "Flow BOM private type",
    ),
    # CSS Object Model types
    print_type_format("CSSRule", description="Flow CSSOM type"),
    print_type_format("CSSRuleList", description="Flow CSSOM type"),
    print_type_format("CSSStyleDeclaration", description="Flow CSSOM type"),
    print_type_format("CSSStyleSheet", description="Flow CSSOM type"),
    print_type_format("MediaList", description="Flow CSSOM type"),
    print_type_format("StyleSheet", description="Flow CSSOM type"),
    print_type_format("StyleSheetList", description="Flow CSSOM type"),
    print_type_format("TransitionEvent", description="Flow CSSOM type"),
    # indexedDB types
    print_type_format("IDBCursor", description="Flow indexedDB type"),
    print_type_format("IDBCursorWithValue", description="Flow indexedDB type"),
    print_type_format("IDBDatabase", description="Flow indexedDB type"),
    print_type_format("IDBDirection", description="Flow indexedDB type"),
    print_type_format("IDBEnvironment", description="Flow indexedDB type"),
    print_type_format("IDBFactory", description="Flow indexedDB type"),
    print_type_format("IDBIndex", description="Flow indexedDB type"),
    print_type_format("IDBKeyRange", description="Flow indexedDB type"),
    print_type_format("IDBObjectStore", description="Flow indexedDB type"),
    print_type_format("IDBOpenDBRequest", description="Flow indexedDB type"),
    print_type_format("IDBRequest", description="Flow indexedDB type"),
    print_type_format("IDBTransaction", description="Flow indexedDB type"),
    # Node.js types
    print_type_format("AssertionError", description="Flow Node.js type"),
    print_type_format("Buffer", description="Flow Node.js type"),
    print_type_format("Sign", description="Flow Node.js type"),
    print_type_format("Verify", description="Flow Node.js type"),
    print_type_format("duplexStreamOptions", description="Flow Node.js type"),
    print_type_format("EventEmitter", description="Flow Node.js type"),
    print_type_format("FSWatcher", description="Flow Node.js type"),
    print_type_format("ReadStream", description="Flow Node.js type"),
    print_type_format("Stats", description="Flow Node.js type"),
    print_type_format("WriteStream", description="Flow Node.js type"),
    print_type_format("ClientRequest", description="Flow Node.js type"),
    print_type_format("IncomingMessage", description="Flow Node.js type"),
    print_type_format("Server", description="Flow Node.js type"),
    print_type_format("ServerResponse", description="Flow Node.js type"),
    print_type_format("ClientRequest", description="Flow Node.js type"),
    print_type_format("IncomingMessage", description="Flow Node.js type"),
    print_type_format("Server", description="Flow Node.js type"),
    print_type_format("ServerResponse", description="Flow Node.js type"),
    print_type_format("Server", description="Flow Node.js type"),
    print_type_format("Socket", description="Flow Node.js type"),
    print_type_format("Process", description="Flow Node.js type"),
    print_type_format(
        "readableStreamOptions", description="Flow Node.js type"
    ),
    print_type_format(
        "writableStreamOptions", description="Flow Node.js type"
    ),
    print_type_format("Deflate", description="Flow Node.js type"),
    print_type_format("DeflateRaw", description="Flow Node.js type"),
    print_type_format("Gunzip", description="Flow Node.js type"),
    print_type_format("Gzip", description="Flow Node.js type"),
    print_type_format("Inflate", description="Flow Node.js type"),
    print_type_format("InflateRaw", description="Flow Node.js type"),
    print_type_format("Unzip", description="Flow Node.js type"),
    print_type_format("Zlib", description="Flow Node.js type"),
    # Node.js private types
    print_type_format(
        "bufferEncoding", "buffer\$Encoding", "Flow Node.js private type"
    ),
    print_type_format(
        "bufferNonBufferEncoding",
        "buffer\$NonBufferEncoding",
        "Flow Node.js private type",
    ),
    print_type_format(
        "bufferToJSONRet", "buffer\$ToJSONRet", "Flow Node.js private type"
    ),
    print_type_format(
        "child_processChildProcess",
        "child_process\$ChildProcess",
        "Flow Node.js private type",
    ),
    print_type_format(
        "child_processError",
        "child_process\$Error",
        "Flow Node.js private type",
    ),
    print_type_format(
        "child_processexecCallback",
        "child_process\$execCallback",
        "Flow Node.js private type",
    ),
    print_type_format(
        "child_processexecFileCallback",
        "child_process\$execFileCallback",
        "Flow Node.js private type",
    ),
    print_type_format(
        "child_processexecFileOpts",
        "child_process\$execFileOpts",
        "Flow Node.js private type",
    ),
    print_type_format(
        "child_processexecFileSyncOpts",
        "child_process\$execFileSyncOpts",
        "Flow Node.js private type",
    ),
    print_type_format(
        "child_processexecOpts",
        "child_process\$execOpts",
        "Flow Node.js private type",
    ),
    print_type_format(
        "child_processexecSyncOpts",
        "child_process\$execSyncOpts",
        "Flow Node.js private type",
    ),
    print_type_format(
        "child_processforkOpts",
        "child_process\$forkOpts",
        "Flow Node.js private type",
    ),
    print_type_format(
        "child_processHandle",
        "child_process\$Handle",
        "Flow Node.js private type",
    ),
    print_type_format(
        "child_processspawnOpts",
        "child_process\$spawnOpts",
        "Flow Node.js private type",
    ),
    print_type_format(
        "child_processspawnRet",
        "child_process\$spawnRet",
        "Flow Node.js private type",
    ),
    print_type_format(
        "child_processspawnSyncOpts",
        "child_process\$spawnSyncOpts",
        "Flow Node.js private type",
    ),
    print_type_format(
        "child_processspawnSyncRet",
        "child_process\$spawnSyncRet",
        "Flow Node.js private type",
    ),
    print_type_format(
        "clustersetupMasterOpts",
        "cluster\$setupMasterOpts",
        "Flow Node.js private type",
    ),
    print_type_format(
        "clusterWorker", "cluster\$Worker", "Flow Node.js private type"
    ),
    print_type_format(
        "cryptoCipher", "crypto\$Cipher", "Flow Node.js private type"
    ),
    print_type_format(
        "cryptocreateCredentialsDetails",
        "crypto\$createCredentialsDetails",
        "Flow Node.js private type",
    ),
    print_type_format(
        "cryptoCredentials", "crypto\$Credentials", "Flow Node.js private type"
    ),
    print_type_format(
        "cryptoDecipher", "crypto\$Decipher", "Flow Node.js private type"
    ),
    print_type_format(
        "cryptoDiffieHellman",
        "crypto\$DiffieHellman",
        "Flow Node.js private type",
    ),
    print_type_format(
        "cryptoHash", "crypto\$Hash", "Flow Node.js private type"
    ),
    print_type_format(
        "cryptoHmac", "crypto\$Hmac", "Flow Node.js private type"
    ),
    print_type_format(
        "cryptoSign", "crypto\$Sign", "Flow Node.js private type"
    ),
    print_type_format(
        "cryptoSignprivate_key",
        "crypto\$Sign\$private_key",
        "Flow Node.js private type",
    ),
    print_type_format(
        "cryptoVerify", "crypto\$Verify", "Flow Node.js private type"
    ),
    print_type_format(
        "dgramSocket", "dgram\$Socket", "Flow Node.js private type"
    ),
    print_type_format(
        "domainDomain", "domain\$Domain", "Flow Node.js private type"
    ),
    print_type_format(
        "eventsEventEmitter",
        "events\$EventEmitter",
        "Flow Node.js private type",
    ),
    print_type_format(
        "httpClientRequest", "http\$ClientRequest", "Flow Node.js private type"
    ),
    print_type_format(
        "httpIncomingMessage",
        "http\$IncomingMessage",
        "Flow Node.js private type",
    ),
    print_type_format(
        "httpServerResponse",
        "http\$ServerResponse",
        "Flow Node.js private type",
    ),
    print_type_format(
        "netconnectOptions", "net\$connectOptions", "Flow Node.js private type"
    ),
    print_type_format("netServer", "net\$Server", "Flow Node.js private type"),
    print_type_format("netSocket", "net\$Socket", "Flow Node.js private type"),
    print_type_format(
        "netSocketaddress", "net\$Socket\$address", "Flow Node.js private type"
    ),
    print_type_format("osCPU", "os\$CPU", "Flow Node.js private type"),
    print_type_format(
        "osNetIFAddr", "os\$NetIFAddr", "Flow Node.js private type"
    ),
    print_type_format(
        "osUserInfobuffer", "os\$UserInfo\$buffer", "Flow Node.js private type"
    ),
    print_type_format(
        "osUserInfostring", "os\$UserInfo\$string", "Flow Node.js private type"
    ),
    print_type_format(
        "readlineInterface", "readline\$Interface", "Flow Node.js private type"
    ),
    print_type_format(
        "streamDuplex", "stream\$Duplex", "Flow Node.js private type"
    ),
    print_type_format(
        "streamPassThrough", "stream\$PassThrough", "Flow Node.js private type"
    ),
    print_type_format(
        "streamReadable", "stream\$Readable", "Flow Node.js private type"
    ),
    print_type_format(
        "streamStream", "stream\$Stream", "Flow Node.js private type"
    ),
    print_type_format(
        "streamTransform", "stream\$Transform", "Flow Node.js private type"
    ),
    print_type_format(
        "streamWritable", "stream\$Writable", "Flow Node.js private type"
    ),
    print_type_format(
        "string_decoderStringDecoder",
        "string_decoder\$StringDecoder",
        "Flow Node.js private type",
    ),
    print_type_format("tlsServer", "tls\$Server", "Flow Node.js private type"),
    print_type_format(
        "tlsTLSSocket", "tls\$TLSSocket", "Flow Node.js private type"
    ),
    print_type_format(
        "ttyReadStream", "tty\$ReadStream", "Flow Node.js private type"
    ),
    print_type_format(
        "ttyWriteStream", "tty\$WriteStream", "Flow Node.js private type"
    ),
    print_type_format("vmContext", "vm\$Context", "Flow Node.js private type"),
    print_type_format("vmScript", "vm\$Script", "Flow Node.js private type"),
    print_type_format(
        "vmScriptOptions", "vm\$ScriptOptions", "Flow Node.js private type"
    ),
    print_type_format(
        "zlibasyncFn", "zlib\$asyncFn", "Flow Node.js private type"
    ),
    print_type_format(
        "zliboptions", "zlib\$options", "Flow Node.js private type"
    ),
    print_type_format(
        "zlibsyncFn", "zlib\$syncFn", "Flow Node.js private type"
    ),
    # Service Workers types
    print_type_format("Cache", description="Flow service worker type"),
    print_type_format(
        "CacheQueryOptions", description="Flow service worker type"
    ),
    print_type_format("CacheStorage", description="Flow service worker type"),
    print_type_format("Client", description="Flow service worker type"),
    print_type_format(
        "ClientQueryOptions", description="Flow service worker type"
    ),
    print_type_format("Clients", description="Flow service worker type"),
    print_type_format("ClientType", description="Flow service worker type"),
    print_type_format(
        "ExtendableEvent", description="Flow service worker type"
    ),
    print_type_format("FetchEvent", description="Flow service worker type"),
    print_type_format(
        "ForeignFetchOptions", description="Flow service worker type"
    ),
    print_type_format("FrameType", description="Flow service worker type"),
    print_type_format("InstallEvent", description="Flow service worker type"),
    print_type_format(
        "NavigationPreloadManager", description="Flow service worker type"
    ),
    print_type_format(
        "NavigationPreloadState", description="Flow service worker type"
    ),
    print_type_format(
        "RegistrationOptions", description="Flow service worker type"
    ),
    print_type_format("RequestInfo", description="Flow service worker type"),
    print_type_format("ServiceWorker", description="Flow service worker type"),
    print_type_format(
        "ServiceWorkerContainer", description="Flow service worker type"
    ),
    print_type_format(
        "ServiceWorkerMessageEvent", description="Flow service worker type"
    ),
    print_type_format(
        "ServiceWorkerRegistration", description="Flow service worker type"
    ),
    print_type_format(
        "ServiceWorkerState", description="Flow service worker type"
    ),
    print_type_format(
        "VisibilityState", description="Flow service worker type"
    ),
    print_type_format("WindowClient", description="Flow service worker type"),
    print_type_format("WorkerType", description="Flow service worker type"),
    # Streams types
    print_type_format("PipeToOptions", description="Flow streams type"),
    print_type_format("QueuingStrategy", description="Flow streams type"),
    print_type_format(
        "ReadableByteStreamController", description="Flow streams type"
    ),
    print_type_format("ReadableStream", description="Flow streams type"),
    print_type_format(
        "ReadableStreamBYOBRequest", description="Flow streams type"
    ),
    print_type_format(
        "ReadableStreamController", description="Flow streams type"
    ),
    print_type_format("ReadableStreamReader", description="Flow streams type"),
    print_type_format("TextEncodeOptions", description="Flow streams type"),
    print_type_format("TextEncoder", description="Flow streams type"),
    print_type_format("TransformStream", description="Flow streams type"),
    print_type_format("UnderlyingSink", description="Flow streams type"),
    print_type_format("UnderlyingSource", description="Flow streams type"),
    print_type_format("WritableStream", description="Flow streams type"),
    print_type_format(
        "WritableStreamController", description="Flow streams type"
    ),
    print_type_format("WritableStreamWriter", description="Flow streams type"),
]
