from errors import *
from datetime import datetime, timedelta
import re


class User:
    def __init__(self, name, email, password, birthday):
        self.name = name
        self.email = email
        self.password = password
        self.birthday = birthday
        self.created_at = datetime.now()

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError(f'setter for name must receive str and got type {type(value)} {value}')
        if len(value) < 4:
            raise UserNameTooShortError(f'setter for name must get str with len 4. \nvalue=  {value} \nlen = {len(value)}\n')
        if not any(c.isalpha() for c in value):
            raise NameNonCharError(f'setter for name must have at least one letter. value={value}\n')
        self.__name = value

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        if not isinstance(value, str):
            raise TypeError(f'setter for email must receive str and got type {type(value)} \nand value: {value}\n')
        if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', value):
            raise IllegalEmailFormatError(f'an email address must contain @ and . chars \nthis address {value} does not\n')
        self.__email = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        if not isinstance(value, str):
            raise TypeError(f'setter for password must receive str and got type {type(value)} {value}')
        # if len(value) < 8: raise IllegalPasswordFormatError(f'setter for password must get str with len 8. value=
        # {value} len = {len(value)}')
        if not re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$', value):
            raise IllegalPasswordFormatError(
                f'setter for password must get str with len 8 (at least) and must contain one upper case, one lower '
                f'case and one special char. \npassword value = {value} \npassword len = {len(value)}\n')
        self.__password = value

    @property
    def birthday(self):
        return self.__birthday

    @birthday.setter
    def birthday(self, birth_date):
        if isinstance(birth_date, str):
            birth_date = parse_date(birth_date)
        if isinstance(birth_date, datetime):
            if not birth_date < datetime.now():
                raise IllegalBirthdayError(f'birthday must be in the past not {birth_date}\n')
            elif datetime.now() - timedelta(days=365 * 20) < birth_date:
                raise UserTooYoungError(f"user must be at least 20 years old: {birth_date}\n")
            else:
                self.__birthday = birth_date

        else:
            raise TypeError(f"birthday must be a datetime object or valid string, not {type(birth_date)}")

    @property
    def age(self):
        return (datetime.now() - self.__birthday).year


def parse_date(date_str):
    # print("in parse date")
    formats = ["%Y-%m-%d", "%d/%m/%Y", "%m-%d-%Y", "%d-%m-%Y", "%d.%m.%Y"]
    for fmt in formats:
        try:
            # print("out parse date")
            return datetime.strptime(date_str, fmt)
        except ValueError:
            continue
    raise ValueError(f"Date string {date_str} does not match any known formats.")
