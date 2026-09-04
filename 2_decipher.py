encoded = """
   !!junk-77!! | [3::DW::ok] | [xx::DRSC::bad] |
   [1::NFFU::ok] | ##nothing## | [5::TQI_QNGWFWD::ok] |
   [2::OG::ok] | [4::XLI::ok] | [7::WT7::bad] |
   [6::GZ_7_VS::ok] | [99::IGNORE_ME::bad] | %%noise%%
"""

###############################################################
"""
1. Part of the real message is inside the the '[' and ']' brackets.
2. Each fragment inside the brackets has a number, jumbled text of the message, and 'ok'. Focus on only those fragments. The '::' are just separating these parts in the fragment 
3. To find the actual message in every fragment,take every letter in the jumbled message, and shift it backward by the number part in that fragment
For example, if the number is 3 and the jumbled message is ABC, then the actual message is XYZ.
Similarly, if the number is 5 and the jumbled message is ABC, then the actual message is VWX.
4. Ignore any fragment that has 'bad' instead of 'ok'.
5. Once you have decoded all the fragments, combine them in the order of their numbers to get the final message. First comes the fragment with number 1, then 2, and so on.
"""

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


fragments = []

temp_parts = encoded.split("[")

for part in temp_parts:
    if "::ok]" in part:
        before_bracket = part.split("]")[0]
        
        segment_parts = before_bracket.split("::")
        
        if len(segment_parts) == 3 and segment_parts[2] == "ok":
            num_str = segment_parts[0]
            cipher_text = segment_parts[1]
            
            is_number = True
            for ch in num_str:
                if ch < '0' or ch > '9':
                    is_number = False
                    break
            
            if is_number:
                num = 0
                for ch in num_str:
                    num = num * 10 + (ord(ch) - ord('0'))
                
                fragments.append((num, cipher_text))

for i in range(len(fragments)):
    min_idx = i
    for j in range(i + 1, len(fragments)):
        if fragments[j][0] < fragments[min_idx][0]:
            min_idx = j
    temp = fragments[i]
    fragments[i] = fragments[min_idx]
    fragments[min_idx] = temp

decoded_fragments = []

for num, cipher_text in fragments:
    decoded_chars = []
    
    for ch in cipher_text:
        if ch in alphabet:
            for i in range(len(alphabet)):
                if alphabet[i] == ch:
                    idx = i
                    break
            
            new_idx = (idx - num) % 26
            decoded_chars.append(alphabet[new_idx])
        else:
            decoded_chars.append(ch)
    
    decoded_text = ""
    for ch in decoded_chars:
        decoded_text = decoded_text + ch
    
    decoded_fragments.append((num, decoded_text))

final_message = ""
for i in range(len(decoded_fragments)):
    final_message = final_message + decoded_fragments[i][1]

for num, text in decoded_fragments:
    print(str(num) + ": " + text)

print(final_message)
