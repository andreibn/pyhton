from email import message


name = " eric ";
name = name.rstrip();
name = name.lstrip();
print(f"Hello {name}, would you like to learn some Python today?");
print(name.upper());
print(name.lower());
# выводит с заглавной буквы
print(name.capitalize());

famous_person = ' Albert Einstein ';
message = f'\t{famous_person} once said, "A person who never made \n\ta mistake never tried anything new."';
print(message);
famous_person = famous_person.strip();
message = f'\t{famous_person} once said, "A person who never made \n\ta mistake never tried anything new."';
print(message);