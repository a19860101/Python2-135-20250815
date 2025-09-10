import re

email  = input('email:')

# 一個常用的 email 正規表達式模式
# 這個模式匹配常見的電子郵件格式，例如：name@domain.com
email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

def is_valid_email(email):
    """
    使用正規表達式驗證電子郵件地址。
    """
    if re.match(email_pattern, email):
        return True
    else:
        return False

# 範例使用
#
# email1 = "test@example.com"
# email2 = "invalid-email@"
# email3 = "user.name+tag@subdomain.domain.co.uk"
# print(f"'{email1}' 是有效的郵箱嗎？ {is_valid_email(email1)}")
# print(f"'{email2}' 是有效的郵箱嗎？ {is_valid_email(email2)}")
# print(f"'{email3}' 是有效的郵箱嗎？ {is_valid_email(email3)}")
print(f"'{email}' 是有效的郵箱嗎？ {is_valid_email(email)}")