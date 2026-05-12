def pangkat(basis, eksponen):
    # base case: bilangan apa pun pangkat 0 hasilnya adalah 1
    if eksponen == 0:
        return 1
    # base case: bilangan pangkat 1 adalah bilangan itu sendiri
    elif eksponen == 1:
        return basis
    else:
        # rekursi: kalikan basis dengan hasil fungsi pangkat (eksponen dikurang 1)
        return basis * pangkat(basis, eksponen - 1)

# contoh penggunaan
basis = 2
eksponen = 3
hasil = pangkat(basis, eksponen)

print(f"{basis}^{eksponen} = {hasil}")
# logikanya: 2^3 = 2 * (2^2) = 2 * (2 * (2^1)) = 2 * (2 * 2) = 8