def hammingWeight(n: int) -> int:
    binary_n: str = f"{n:b}"
    num_of_1: int = 0
    for i in range(len(binary_n)):
        if binary_n[i] == "1":
            num_of_1 += 1
    return num_of_1

def main() -> None:
    print(hammingWeight(11))
    print(hammingWeight(128))
    print(hammingWeight(2147483645))

if __name__ == "__main__":
    main()