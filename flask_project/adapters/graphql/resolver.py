from ariadne import MutationType
from application.UseCases.register_user import register_user_use_case
from application.UseCases.login_user import login_user_use_case

mutation = MutationType()

@mutation.field("registerUser")
def resolve_register_user(_, info, email, password, username, name):
    result = register_user_use_case(email, password, username, name)
    return result

@mutation.field("loginUser")
def resolve_login_user(_, info, email, password):
    result1 = login_user_use_case(email, password)
    return result1