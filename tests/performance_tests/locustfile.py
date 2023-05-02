from locust import HttpUser, task


class ProjectPerfTest(HttpUser):

    @task
    def test_index(self):
        self.client.get('/')

    @task
    def test_summary(self):
        self.client.post('/show_summary', data={'email': 'john@simplylift.co'})

    @task
    def test_book(self):
        self.client.get('/book/Spring Festival/Simply Lift')

    @task
    def test_purchase(self):
        self.client.post('/purchase_places', data={'club': 'Simply Lift',
                                                   'competition': 'Spring Festival', 'places': '1'})

    @task
    def test_rankings(self):
        self.client.get('/show_points')

    @task
    def test_logout(self):
        self.client.get('/logout')
