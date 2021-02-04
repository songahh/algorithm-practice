"""
    금지된 단어를 제외한 가장 흔하게 등장하는 단어를 출력하라.
    대소문자 구분을 하지 않으며, 구두점(마침표, 쉼표 등) 또한 무시한다.

    Input:
        paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
        banned = ["hit"]
    Output: "ball"

    Input:
        paragraph = "a, a, a, a, b,b,b,c, c"
        banned = ["a"]
    Output: b

    Input:
        paragraph = "abc abc? abcd the jeff!"
        banned = ["abc","abcd","jeff"]
    Output = "the"

    Input:
        paragraph = "Z? Z, Z. S. O. z; X, R. k? X, R' M! D! i. W, p. X, t; s, U; T? Z? W! X, O. g, M; y? t; X; O, X' C' Y; x! q! Y' T; u? R. j? w, M. F' n' F; y, V' z. R, V; x' y? F' m' p? M. w, n! Y' Y? i. S' P? w; w; y! Z; P' o? I, H! L; U; p' i; s' Z. V; S! V! H! y' I? K; d. L! r? u! U. O! s? j. y. G, g, r; Z, X, x' L! l? Z, w! Z' W! b. N! T. P! Y, Z. u! Z, q! Y? P' G' u' t, N' k, H' T, I. S' q? J. q! i? E! Q. O, j' r; r' L' C, z! G, p. S. p' s' L! u. S. t, V; z, Z' p! t? Z. x! h; T; T' V, w; P? Q' T! q. J; E? n. V' X. M? Q, v; U; O, H? h; T. s, n! Y? a, N; o, V, o. S! K' j! Y, W! v; Q! u? U' l. k. r, o. o; m. E, I. n! H' w? u? x! w! U' m; w; R' n. y. Y, W' d; P? z! K! g? m, J' i. t, j. x! F. F' U? K! r' V, r, s! O, Q, v, v, c. E. s! X. k; F' Y! r? P! g! r! V! w; S! X, S! N, z? m. y. B; Y' n' U? r. u; R. l? U? v, r, y' W' W' Q; n' Y? Z, L? O. T? Q' q. l, z! V. T. k; x' q! s; u? W! x' X; P; m! t; T? X, v, v' t. Y' q; X? u; V; X! q! w. j! W; z; v. u, j. w; v. z; W' P' z; l! l. o! Z, Y. H; Q; k' O' m, U!"
        banned = ["c","y","u","i","p","j","g","r","o","h","t","m","k","z","s","q","v","a","e","x"]
"""
import re

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:

        paragraph = re.sub(",", " ", paragraph)
        paragraph = re.sub("[^a-zA-Z0-9 ]", "", paragraph)
        paragraph = paragraph.lower()
        list1 = paragraph.split()

        for word in banned:
            while word in list1:
                list1.remove(word)

        max_string = 0
        max_count = list1.count(list1[0])

        for i in range(1, len(list1)):
            if list1.count(list1[i]) > max_count:
                max_string = i
                max_count = list1.count(list1[i])

        return list1[max_string]