class SeshTerminator:
    server = None
    credential = None
    tenant = None

    def __init__(self, server=None, credential=None, tenant=None):
        if server:
            self.server = server

        if credential:
            self.credential = credential

        if tenant:
            self.tenant = tenant

    def terminate_all_sessions(self, identifier) -> None:
        pass

    def terminate_session(self, userid, session) -> None:
        pass

    def get_user_sessions(self, identifier: str) -> list:
        pass

    def delete_user(self, identifier) -> None:
        # kill sessions, then delete
        pass

    def disable_user(self, identifier) -> None:
        # kill sessions, then disable
        pass

    def lookup_user_id_by_email(self, user_email: str) -> str:
        return user_email
