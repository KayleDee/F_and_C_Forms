from django.test import SimpleTestCase


# Create your tests here.
class TestFrontTimes(SimpleTestCase):
    def testChoCho2(self):
        response = self.client.get("/warmup-2/front_times/?num=2&words=Chocolate")
        self.assertContains(response, "ChoCho")
    def testChoChoCho3(self):
        response = self.client.get("/warmup-2/front_times/?num=3&words=Chocolate")
        self.assertContains(response, "ChoChoCho")
    def testAbc3(self):
        response = self.client.get("/warmup-2/front_times/?num=3&words=Abc")
        self.assertContains(response, "AbcAbcAbc")
class Test_No_Teen_Sum(SimpleTestCase):
     def test123(self):
        response = self.client.get("/logic-2/no-teen-sum/?a=1&b=2&c=3")
        self.assertContains(response, 6)
     def test2114(self):
        response = self.client.get("/logic-2/no-teen-sum/?a=2&b=1&c=14")
        self.assertContains(response, 3)
     def test2119(self):
        response = self.client.get("/logic-2/no-teen-sum/?a=2&b=1&c=17")
        self.assertContains(response, 3)
class Test_XYZ_Theres(SimpleTestCase):
    def testxy(self):
        response = self.client.get("/string-2/xyz-there/?xyz=xy")
        self.assertContains(response, False)
    def testx(self):
        response = self.client.get("/string-2/xyz-there/?xyz=x")
        self.assertContains(response, False)
    def testxyz(self):
        response = self.client.get("/string-2/xyz-there/?xyz=xyz")
        self.assertContains(response, True)
class Test_Centered_Average(SimpleTestCase):
     def test1(self):
        response = self.client.get("/list-2/centered-average/?nums1=1&nums2=1&nums3=100")
        self.assertContains(response, 1.0)
     def test4(self):
        response = self.client.get("/list-2/centered-average/?nums1=4&nums2=0&nums3=4")
        self.assertContains(response, 4.0)
     def test7(self):
        response = self.client.get("/list-2/centered-average/?nums1=7&nums2=7&nums3=7")
        self.assertContains(response, 7.0)

