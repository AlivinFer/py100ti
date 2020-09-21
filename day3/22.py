# 函数调用
def hello_world():
    print("hello world")

def n_hello(n):
    for i in range(n):
        hello_world()


if __name__ == "__main__":
    n_hello(5)