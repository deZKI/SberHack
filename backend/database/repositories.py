from elasticsearch_dsl import Search

from shemas import ResumeSchema
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

    @staticmethod
    def get_resume_by_content(content: str):
        search = Search(index='resumes')
        search = search.query("match", content=content)
        response = search.execute()
        results = [ResumeSchema(content=hit.content, score=hit.meta.score) for hit in response]
        return results
