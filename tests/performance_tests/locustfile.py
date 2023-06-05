from locust import HttpUser, task

class ProjectPerfTest(HttpUser):

    @task
    def retrieve_competitions(self):
        self.client.post(
            "/showSummary",
            data={"email": "admin@irontemple.com"},
        )

    @task
    def update_points(self):
        self.client.post(
            "/purchasePlaces",
            data={
                "competition": "Spring Festival",
                "club": "Simply Lift",
                "places": 2,
            },
        )