encoded = """
   !!junk-77!! | [3::DW::ok] | [xx::DRSC::bad] |
   [1::NFFU::ok] | ##nothing## | [5::TQI_QNGWFWD::ok] |
   [2::OG::ok] | [4::XLI::ok] | [7::WT7::bad] |
   [6::GZ_7_VS::ok] | [99::IGNORE_ME::bad] | %%noise%%
"""
import re
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
pattern = r'\[([^]]+)\]'
matches = re.findall(pattern, encoded)
fragments = []
for match in matches:
    parts = match.split('::')
    if len(parts) != 3:
        continue
    num_str, text, status = parts
    if status != 'ok' or not num_str.isdigit():
        continue
    num = int(num_str)
    fragments.append((num, text))
fragments.sort(key=lambda x: x[0])
def shift_backward(text, shift):
    result = []
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            new_ord = (ord(ch) - base - shift) % 26 + base
            result.append(chr(new_ord))
        else:
            result.append(ch)
    return ''.join(result)
decoded_parts = []
for num, text in fragments:
    decoded = shift_backward(text, num)
    decoded_parts.append((num, decoded))
final_message = ''.join([part for _, part in sorted(decoded_parts)])
print(final_message)

