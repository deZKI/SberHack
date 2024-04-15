import json

from .models import Resume


class ResumeRepositories:
    @staticmethod
    def add_resume(content: str) -> str:
        resume = Resume(content=content)
        resume.save()
        return resume.meta.id

    @staticmethod
    def get_all_resumes() -> list[str]:
        search = Resume.search()
        response = search.execute()
        resumes = []
        for hit in response:
            resumes.append(hit.content)
        return resumes
