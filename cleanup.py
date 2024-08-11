def get_chars():
    chars = []

    # Append symbols and punctuation first
    chars.append(chr(0x000A)) # Newline character
    chars.append(chr(0x0020)) # Space
    chars.append(chr(0x0021)) # Exclamation mark
    chars.append(chr(0x0022)) # Double quotation mark
    chars.append(chr(0x0026)) # Ampersand
    chars.append(chr(0x0027)) # Apostrophe (Glottal stop for Kayan orthography)
    chars.append(chr(0x0028)) # Left parenthesis
    chars.append(chr(0x0029)) # Right parenthesis
    chars.append(chr(0x003A)) # Colon
    chars.append(chr(0x003F)) # Question mark

    # Confusables - These characters look similar to the Kayan glottal stop character, typically typed with U+0027
    chars.append(chr(0x0060)) # Grave accent (in case an apostrophe was mistaken as a grave accent)
    chars.append(chr(0x00B4)) # Accute Accent
    chars.append(chr(0x02B9)) # Modifier Letter Prime
    chars.append(chr(0x02BB)) # Modifier Letter Turned Comma
    chars.append(chr(0x02BC)) # Modifier Letter Apostrophe
    chars.append(chr(0x02BD)) # Modifier Letter Reversed Comma
    chars.append(chr(0x02BE)) # Modifier Letter Right Half Ring
    chars.append(chr(0x02C8)) # Modifier Letter Vertical Line
    chars.append(chr(0x02CA)) # Modifier Letter Acute Accent
    chars.append(chr(0x02CB)) # Modifier Letter Grave Accent
    chars.append(chr(0x02F4)) # Modifier Letter Middle Grave Accent
    chars.append(chr(0x0374)) # Greek Numeral Sign
    chars.append(chr(0x0384)) # Greek Tonos
    chars.append(chr(0x055A)) # Armenian Apostrophe
    chars.append(chr(0x055D)) # Armenian Comma
    chars.append(chr(0x05D9)) # Hebrew Letter Yod
    chars.append(chr(0x05F3)) # Hebrew Punctuation Geresh
    chars.append(chr(0x07F4)) # Nko High Tone Apostrophe
    chars.append(chr(0x07F5)) # Nko Low Tone Apostrophe
    chars.append(chr(0x144A)) # Canadian Syllabics West-Cree P
    chars.append(chr(0x16CC)) # Runic Letter Short-Twig-Sol S
    chars.append(chr(0x1FBD)) # Greek Koronis
    chars.append(chr(0x1FBF)) # Greek Psili
    chars.append(chr(0x1FEF)) # Greek Varia
    chars.append(chr(0x1FFD)) # Greek Oxia
    chars.append(chr(0x1FFE)) # Greek Dasia
    chars.append(chr(0x2018)) # Left Single Quotation Mark
    chars.append(chr(0x2019)) # Right Single Quotation Mark
    chars.append(chr(0x201B)) # Single High-Reversed-9 Quotation Mark
    chars.append(chr(0x2032)) # Prime
    chars.append(chr(0x2035)) # Reversed Prime
    chars.append(chr(0xA78C)) # Latin Small Letter Saltillo
    chars.append(chr(0x16F51)) # Miao Sign Aspiration
    chars.append(chr(0x16F52)) # Miao Sign Reformed Voicing
    chars.append(chr(0xFF07)) # Fullwidth Apostrophe
    chars.append(chr(0xFF40)) # Fullwidth Grave Accents
    

    # Append digits
    reached = False
    begin = 0x0030 # Digit 0
    end = 0x0039 # Digit 9
    index = begin
    while (reached == False):
        chars.append(chr(index))
        if (index == end):
            reached = True
        else:
            index = index + 0x0001

    
    # Append uppercase letters
    reached = False
    begin = 0x0041 # Uppercase A
    end = 0x005A # Uppercase Z
    index = begin
    while (reached == False):
        chars.append(chr(index))
        if (index == end):
            reached = True
        else:
            index = index + 0x0001
    
    chars.append(chr(0x00C9)) # Append uppercase É


    # Append lowercase letters
    reached = False
    begin = 0x0061 # Lowercase a
    end = 0x007A # Lowercase z
    index = begin
    while (reached == False):
        chars.append(chr(index))
        if (index == end):
            reached = True
        else:
            index = index + 0x0001
    
    chars.append(chr(0x00E9)) # Append lowercase é

    return chars

print("Everything EXCEPT the following characters will be removed: ")
print(get_chars())

def filter_characters(input_file, output_file, allowed_chars):
  """Removes all characters except those in allowed_chars from input_file and writes to output_file.

  Args:
    input_file: The path to the input text file.
    output_file: The path to the output text file.
    allowed_chars: A list of allowed characters.
  """

  with open(input_file, 'r') as f_in, open(output_file, 'w') as f_out:
    for line in f_in:
      filtered_line = ''.join(char for char in line if char in allowed_chars)
      f_out.write(filtered_line)

allowed_characters = get_chars()
input_filename = 'output_part1.txt'
output_filename = 'part1_cleaned.txt'

print("Filtering ", input_filename)
filter_characters(input_filename, output_filename, allowed_characters)
print("Done. Stored as ", output_filename)

