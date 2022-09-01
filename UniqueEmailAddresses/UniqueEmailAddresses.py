class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        set_ = set()
        for email in emails:
            local, domain = email.split("@")
            local = local.split('+')[0]
            local = local.replace('.', '')
            set_.add(local + '@' + domain)
        return len(set_)
