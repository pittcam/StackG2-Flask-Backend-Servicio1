from adapters.out.supabase.auth_service import register_user_with_supabase

def register_user_use_case(email, password, username, name):
    return register_user_with_supabase(email, password, username, name)
