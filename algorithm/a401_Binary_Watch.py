import os


class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        h = {0: ['0'],
             1: ['1', '2', '4', '8'],
             2: ['3', '5', '6', '9', '10'],
             3: ['7', '11']}

        m = {0: ['00'],
             1: ['01', '02', '04', '08', '16', '32'],
             2: ['03', '05', '06', '09', '10', '12', '17', '18', '20', '24', '33', '34', '36', '40', '48'],
             3: ['07', '11', '13', '14', '19', '21', '22', '25', '26', '28', '35', '37', '38', '41', '42', '44', '49',
                 '50',
                 '52', '56'],
             4: ['15', '23', '27', '29', '30', '39', '43', '45', '46', '51', '53', '54', '57', '58'],
             5: ['31', '47', '55', '59']
             }

        m1 = num
        ans = []
        while m1 >= 0:
            h1 = num - m1
            if m1 in m and h1 in h:
                for hh in h[h1]:
                    for mm in m[m1]:
                        ans.append(hh + ':' + mm)
            m1 -= 1
        return ans


if __name__ == "__main__":
    print("Running", os.path.basename(__file__), end=' ')
    acutal_res = Solution().readBinaryWatch(1)
    expected_res = ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]
    assert len(acutal_res) == len(expected_res) and len(set(acutal_res).difference(set(expected_res))) == 0
    print(" ---> Success")
