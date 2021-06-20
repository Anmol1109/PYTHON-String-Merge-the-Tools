def merge_the_tools(string, k):
    num = int(len(string) / k)
    for i in range(num):
        t = string[i * k : (i + 1) * k]
        u = ""
        for c in t:
            if c not in u:
                u += c
        print(u)
    # your code goes here

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
