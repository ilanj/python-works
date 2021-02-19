'''
convert list of nos to words and convert them to text, and count vowels in each text and
count how many pair of the input text can sum to that count, and display result as text
'''
no = int(input())
no_to_text = {
    0:"zero", 1:"one", 2:"two",  3:"three", 4:"four", 5:"five", 6:"six", 7:"seven",
    8:"eight", 9:"nine", 10:"ten",11:"eleven", 12:"twelve", 13:"thirteen", 14:"fourteen",
    15:"fifteen", 16:"sixteen", 17:"seventeen", 18:"eighteen", 19:"nineteen", 20:"twenty" , 30: "thirty", 40:"fourty", 50:"fifty",
    60:"sixty", 70:"seventy", 80:"eighty", 90:"ninety",100:"hundred"
}
def no2words(no):
    if no not in no_to_text:
        q = no // 10
        q = q * 10
        r = no % 10
        return no_to_text[q] + " " +no_to_text[r]
    else:
        return no_to_text[no]

print(no2words(no))