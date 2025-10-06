#!/usr/bin/env python3
# Strings Tiny Workshop (~65 lines)

import string

# ---- Exercism core ----
def add_prefix_un(w: str) -> str: return "un" + w
def make_word_group(ws: list[str]) -> str:
    if not ws: return ""
    p = ws[0]; return " :: ".join([p] + [p + w for w in ws[1:]])
def remove_suffix_ness(w: str) -> str:
    if not w.endswith("ness"): return w
    r = w[:-4]; return (r[:-1] + "y") if r.endswith("i") else r
def adjective_to_verb(s: str, i: int) -> str:
    return s.split()[i].strip(string.punctuation) + "en"

# ---- Mini-labs ----
def lab_index_slice():
    s = input("Base: ")
    while True:
        q = input("Index/slice (e.g., 0, -1, 2:5, ::-1; empty=back): ")
        if not q: break
        try:
            if ":" in q:
                a,b,*c = (q+"::").split(":")[:3]
                sl = slice(int(a) if a else None,
                           int(b) if b else None,
                           int(c[0]) if c and c[0] else None)
                print("=>", s[sl])
            else:
                print("=>", s[int(q)])
        except Exception as e:
            print("Oops:", e)

def lab_methods():
    s = input("Base: ")
    print("upper:", s.upper(), "\nlower:", s.lower(),
          "\nstrip:", s.strip(), "\nreplace a->@:", s.replace("a","@"),
          "\n'cat' in s?:", "cat" in s, "\ncount('e'):", s.count("e"))

def lab_split_join():
    parts = input("Sentence: ").split()
    print("split ->", parts)
    print("join ->", input("Joiner (e.g., '-'): ").join(parts))

# ---- Vocab playground ----
def vocab_menu():
    while True:
        print("\nVocab: 1) un+word  2) group  3) -ness  4) adj->verb  0) back")
        c = input("Pick: ").strip()
        if c == "0": break
        elif c == "1":
            print("=>", add_prefix_un(input("word: ").strip()))
        elif c == "2":
            items = [x.strip() for x in input("prefix,list: ").split(",") if x.strip()]
            print("=>", make_word_group(items))
        elif c == "3":
            print("=>", remove_suffix_ness(input("word: ").strip()))
        elif c == "4":
            s = input("sentence: "); i = int(input("index: "))
            try: print("=>", adjective_to_verb(s,i))
            except Exception as e: print("Error:", e)

# ---- Main ----
def main():
    print("== STRING SKILLS TINY ==\n1) Index/Slice  2) Methods  3) Split/Join  4) Vocab  0) Exit")
    while True:
        c = input("\nPick: ").strip()
        if c == "0": print("Bye!"); break
        elif c == "1": lab_index_slice()
        elif c == "2": lab_methods()
        elif c == "3": lab_split_join()
        elif c == "4": vocab_menu()
        else: print("0–4 only")

if __name__ == "__main__":
    main()
