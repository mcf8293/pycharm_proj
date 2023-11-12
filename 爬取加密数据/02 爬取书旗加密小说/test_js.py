import execjs

js_code = """
function add(a, b) {
    return a + b;
}
"""

ctx = execjs.compile(js_code)
result = ctx.call("add", 1, 2)
print(result)  # 输出3
