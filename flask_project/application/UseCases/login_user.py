from adapters.out.supabase.auth_service import login_user_with_supabase

def login_user_use_case(email, password):
    return login_user_with_supabase(email, password)
