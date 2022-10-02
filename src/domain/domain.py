import tldextract


def domain_check(enter: dict) -> dict:
    ng = ["tk", "zw", "bd", "ke", "am", "SBS", "date", "pw", "quest", "cd", "bid", "cyou", "support", "win", "rest", "casa", "help", "ml", "ws", "icu", "tokyo", "xyz", "cam", "uno", "email", "stream", "gq", "cf", "su", "cm", "casino", "xxx", "poker", "porn", "best", "sex", "sexy", "adult", "webcam"]

    keys = list(enter.keys())
    values = list(enter.values())
    result = dict()

    for i in range(len(values)):
        # parse
        ext = tldextract.extract(values[i])

        # judgement
        if ext.suffix in ng:
            result.update({keys[i]: {"domain": 1}})
        else:
            result.update({keys[i]: {"domain": 0}})

    return result
