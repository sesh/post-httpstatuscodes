import os
import sys
from thttp import request

API_KEY = os.environ.get("MATAROA_API_KEY")

STATUS_CODES = {
    "100": {
        "reason": "Continue",
        "links": {
            "rfc": "https://datatracker.ietf.org/doc/html/rfc7231#section-6.2.1",
            "mdn": "https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/100",
        },
    },
    "101": {
        "reason": "Switching Protocols",
        "links": {
            "rfc": "https://datatracker.ietf.org/doc/html/rfc7231#section-6.2.2",
            "mdn": "https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/101",
        },
    },
    "103": {
        "reason": "Early Hints",
        "links": {
            "rfc": "https://datatracker.ietf.org/doc/html/rfc8297",
            "mdn": "https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/103",
        },
    },
    "200": {
        "reason": "OK",
        "links": {
            "rfc": "https://datatracker.ietf.org/doc/html/rfc7231#section-6.3.1",
            "mdn": "https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/200",
        },
    },
    "201": {
        "reason": "Created",
        "links": {
            "rfc": "https://datatracker.ietf.org/doc/html/rfc7231#section-6.3.2",
            "mdn": "https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/201",
        },
    },
    "202": {
        "reason": "Accepted",
        "links": {
            "rfc": "https://datatracker.ietf.org/doc/html/rfc7231#section-6.3.3",
            "mdn": "https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/202",
        },
    },
    "203": {
        "reason": "Non-Authoritative Information",
        "links": {
            "rfc": "https://datatracker.ietf.org/doc/html/rfc7231#section-6.3.4",
            "mdn": "https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/203",
        },
    },
    "204": {
        "reason": "No Content",
        "links": {
            "rfc": "https://datatracker.ietf.org/doc/html/rfc7231#section-6.3.5",
            "mdn": "https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/204",
        },
    },
    "205": {
        "reason": "Reset Content",
        "links": {
            "rfc": "https://datatracker.ietf.org/doc/html/rfc7231#section-6.3.6",
            "mdn": "https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/205",
        },
    },
    "206": {
        "reason": "Partial Content",
        "links": {
            "rfc": "https://datatracker.ietf.org/doc/html/rfc7233#section-4.1",
            "mdn": "https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/206",
        },
    },
    "300": {
        "reason": "Multiple Choices",
        "links": {
            "rfc": "https://datatracker.ietf.org/doc/html/rfc7231#section-6.4.1",
            "mdn": "https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/300",
        },
    },
    "301": {
        "reason": "Moved Permanently",
        "links": {
            "rfc": "https://datatracker.ietf.org/doc/html/rfc7231#section-6.4.2",
            "mdn": "https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/301",
        },
    },
    "302": {
        "reason": "Found",
        "links": {
            "rfc": "https://datatracker.ietf.org/doc/html/rfc7231#section-6.4.3",
            "mdn": "https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/302",
        },
    },
    "303": {
        "reason": "See Other",
        "links": {
            "rfc": "https://datatracker.ietf.org/doc/html/rfc7231#section-6.4.4",
            "mdn": "https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/303",
        },
    },
    "304": {
        "reason": "Not Modified",
        "links": {
            "rfc": "https://datatracker.ietf.org/doc/html/rfc7232#section-4.1",
            "mdn": "https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/304",
        },
    },
    "307": {
        "reason": "Temporary Redirect",
        "links": {
            "rfc": "https://datatracker.ietf.org/doc/html/rfc7231#section-6.4.7",
            "mdn": "https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/307",
        },
    },
    "308": {
        "reason": "Permanent Redirect",
        "links": {
            "rfc": "https://datatracker.ietf.org/doc/html/rfc7538",
            "mdn": "https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/308",
        },
    },
    "400": {
        "reason": "Bad Request",
        "links": {
            "rfc": "https://datatracker.ietf.org/doc/html/rfc7231#section-6.5.1",
            "mdn": "https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/400",
        },
    },
    "401": {
        "reason": "Unauthorized",
        "links": {
            "rfc": "https://datatracker.ietf.org/doc/html/rfc7235#section-3.1",
            "mdn": "https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/401",
        },
    },
    "402": {
        "reason": "Payment Required",
        "links": {
            "rfc": "https://datatracker.ietf.org/doc/html/rfc7231#section-6.5.2",
            "mdn": "https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/402",
        },
    },
    "403": {
        "reason": "Forbidden",
        "links": {
            "rfc": "https://datatracker.ietf.org/doc/html/rfc7231#section-6.5.3",
            "mdn": "https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/403",
        },
    },
    "404": {
        "reason": "Not Found",
        "links": {
            "rfc": "https://datatracker.ietf.org/doc/html/rfc7231#section-6.5.4",
            "mdn": "https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/404",
        },
    },
    "405": {
        "reason": "Method Not Allowed",
        "links": {
            "rfc": "https://datatracker.ietf.org/doc/html/rfc7231#section-6.5.5",
            "mdn": "https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/405",
        },
    },
    "406": {
        "reason": "Not Acceptable",
        "links": {
            "rfc": "https://datatracker.ietf.org/doc/html/rfc7231#section-6.5.6",
            "mdn": "https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/406",
        },
    },
    "407": {
        "reason": "Proxy Authentication Required",
        "links": {
            "rfc": "https://datatracker.ietf.org/doc/html/rfc7235#section-3.2",
            "mdn": "https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/407",
        },
    },
    "408": {
        "reason": "Request Timeout",
        "links": {
            "rfc": "https://datatracker.ietf.org/doc/html/rfc7231#section-6.5.7",
            "mdn": "https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/408",
        },
    },
    "409": {
        "reason": "Conflict",
        "links": {
            "rfc": "https://datatracker.ietf.org/doc/html/rfc7231#section-6.5.8",
            "mdn": "https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/409",
        },
    },
    "410": {
        "reason": "Gone",
        "links": {
            "rfc": "https://datatracker.ietf.org/doc/html/rfc7231#section-6.5.9",
            "mdn": "https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/410",
        },
    },
    "411": {
        "reason": "Length Required",
        "links": {
            "rfc": "https://datatracker.ietf.org/doc/html/rfc7231#section-6.5.10",
            "mdn": "https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/411",
        },
    },
    "412": {
        "reason": "Precondition Failed",
        "links": {
            "rfc": "https://datatracker.ietf.org/doc/html/rfc7232#section-4.2",
            "mdn": "https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/412",
        },
    },
    "413": {
        "reason": "Payload Too Large",
        "links": {
            "rfc": "https://datatracker.ietf.org/doc/html/rfc7231#section-6.5.11",
            "mdn": "https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/413",
        },
    },
    "414": {
        "reason": "URI Too Long",
        "links": {
            "rfc": "https://datatracker.ietf.org/doc/html/rfc7231#section-6.5.12",
            "mdn": "https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/414",
        },
    },
    "415": {
        "reason": "Unsupported Media Type",
        "links": {
            "rfc": "https://datatracker.ietf.org/doc/html/rfc7231#section-6.5.13",
            "mdn": "https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/415",
        },
    },
    "416": {
        "reason": "Range Not Satisfiable",
        "links": {
            "rfc": "https://datatracker.ietf.org/doc/html/rfc7233#section-4.4",
            "mdn": "https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/416",
        },
    },
    "417": {
        "reason": "Expectation Failed",
        "links": {
            "rfc": "https://datatracker.ietf.org/doc/html/rfc7231#section-6.5.14",
            "mdn": "https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/417",
        },
    },
    "418": {
        "reason": "I'm a teapot",
        "links": {
            "rfc": "https://datatracker.ietf.org/doc/html/rfc2324",
            "mdn": "https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/418",
        },
    },
    "422": {
        "reason": "Unprocessable Entity",
        "links": {
            "rfc": "https://datatracker.ietf.org/doc/html/rfc4918#section-11.2",
            "mdn": "https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/422",
        },
    },
    "425": {
        "reason": "Too Early",
        "links": {
            "rfc": "https://datatracker.ietf.org/doc/html/rfc8470#section-5.2",
            "mdn": "https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/425",
        },
    },
    "426": {
        "reason": "Upgrade Required",
        "links": {
            "rfc": "https://datatracker.ietf.org/doc/html/rfc7231#section-6.5.15",
            "mdn": "https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/426",
        },
    },
    "428": {
        "reason": "Precondition Required",
        "links": {
            "rfc": "https://datatracker.ietf.org/doc/html/rfc6585#section-3",
            "mdn": "https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/428",
        },
    },
    "429": {
        "reason": "Too Many Requests",
        "links": {
            "rfc": "https://datatracker.ietf.org/doc/html/rfc6585#section-4",
            "mdn": "https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/429",
        },
    },
    "431": {
        "reason": "Request Header Fields Too Large",
        "links": {
            "rfc": "https://datatracker.ietf.org/doc/html/rfc6585#section-5",
            "mdn": "https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/431",
        },
    },
    "451": {
        "reason": "Unavailable For Legal Reasons",
        "links": {
            "rfc": "https://datatracker.ietf.org/doc/html/rfc7725#section-3",
            "mdn": "https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/451",
        },
    },
    "500": {
        "reason": "Internal Server Error",
        "links": {
            "rfc": "https://datatracker.ietf.org/doc/html/rfc7231#section-6.6.1",
            "mdn": "https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/500",
        },
    },
    "501": {
        "reason": "Not Implemented",
        "links": {
            "rfc": "https://datatracker.ietf.org/doc/html/rfc7231#section-6.6.2",
            "mdn": "https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/501",
        },
    },
    "502": {
        "reason": "Bad Gateway",
        "links": {
            "rfc": "https://datatracker.ietf.org/doc/html/rfc7231#section-6.6.3",
            "mdn": "https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/502",
        },
    },
    "503": {
        "reason": "Service Unavailable",
        "links": {
            "rfc": "https://datatracker.ietf.org/doc/html/rfc7231#section-6.6.4",
            "mdn": "https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/503",
        },
    },
    "504": {
        "reason": "Gateway Timeout",
        "links": {
            "rfc": "https://datatracker.ietf.org/doc/html/rfc7231#section-6.6.5",
            "mdn": "https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/504",
        },
    },
    "505": {
        "reason": "HTTP Version Not Supported",
        "links": {
            "rfc": "https://datatracker.ietf.org/doc/html/rfc7231#section-6.6.6",
            "mdn": "https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/505",
        },
    },
    "506": {
        "reason": "Variant Also Negotiates",
        "links": {
            "rfc": "https://datatracker.ietf.org/doc/html/rfc2295#section-8.1",
            "mdn": "https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/506",
        },
    },
    "507": {
        "reason": "Insufficient Storage",
        "links": {
            "rfc": "https://datatracker.ietf.org/doc/html/rfc4918#section-11.5",
            "mdn": "https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/507",
        },
    },
    "508": {
        "reason": "Loop Detected",
        "links": {
            "rfc": "https://datatracker.ietf.org/doc/html/rfc5842#section-7.2",
            "mdn": "https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/508",
        },
    },
    "510": {
        "reason": "Not Extended",
        "links": {
            "rfc": "https://datatracker.ietf.org/doc/html/rfc2774#section-7",
            "mdn": "https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/510",
        },
    },
    "511": {
        "reason": "Network Authentication Required",
        "links": {
            "rfc": "https://datatracker.ietf.org/doc/html/rfc6585#section-6",
            "mdn": "https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/511",
        },
    },
}

md = ""
prev = ""

for code in sorted(STATUS_CODES.keys()):
    if prev and prev[0] != code[0]:
        md += "\n<!-- -->\n\n"
    prev = code[0]

    status_code = STATUS_CODES[code]

    links_md = ", ".join(
        [f"[{name}]({url})" for name, url in status_code["links"].items()]
    )
    md += f"- {code} {status_code['reason']} ({links_md})\n"

md += """\n\n
This post is generated and posted here by a Github action on the [sesh/post-httpstatuscodes](https://github.com/sesh/post-httpstatuscodes) repository.
Pull requests more than welcome to add new status codes or links.

Heavily inspired by httpstatuses.com being redirected to WebFX instead of showing a completely ad-free list of HTTP Status Codes.
"""

# publish
if not API_KEY:
    sys.stderr.write("Missing Mataroa API Key")
    sys.exit(1)
else:
    response = request(
        "https://mataroa.blog/api/posts/http-status-codes/",
        json={
            "body": md,
        },
        headers={"Authorization": f"Bearer {API_KEY}"},
        method="PATCH",
    )
    sys.exit(response.status != 200)
