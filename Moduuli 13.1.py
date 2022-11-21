from flask import Flask, request

app = Flask(__name__)
@app.route('/prime')

def prime():
    args = request.args
    check_num = int(args.get("number"))
    check_status = ""
    if check_num > 1:
        for i in range(2, check_num // 2):
            if(check_num % i) == 0:
                check_status = ("false")
                break
        else:
            check_status = ("true")

    prime_status = {
        "Number": check_num,
        "isPrime": check_status
    }
    return prime_status

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)