from describe_it import describe, it, xit
from hamcrest import *
import io
import file_parser

@describe
def a_schedule_file_parser():

    @it
    def returns_empty_list_if_file_is_empty():
        empty_file = io.StringIO("")
        res = file_parser.parse(empty_file)
        assert_that(res, empty())

    @it
    def parse_one_person():
        file = io.StringIO("1;Nicolette Champlin")
        res = file_parser.parse(file)
        person = res[0]

        assert_that(person.name, equal_to("Nicolette Champlin"))
        assert_that(person.id, equal_to("1"))


    @it
    def parse_person_with_appointment():
        file = io.StringIO('''1;Nicolette Champlin
1;1/8/2015 11:30:00 AM;1/8/2015 2:00:00 PM;ABC''')

        res = file_parser.parse(file)
        person = res[0]

        assert_that(person.id, equal_to("1"))
        assert_that(person.name, equal_to("Nicolette Champlin"))
        assert_that(person.appointments, has_length(1))













#     @it
#     def returns_an_empty_list_if_file_is_empty():
#         empty_file = io.StringIO("")
#         res = file_parser.parse(empty_file)
#         assert_that(res, empty())

#     @it
#     def parse_one_user(): 
#         file = io.StringIO("1;Nicolette Champlin")
#         res = file_parser.parse(file)

#         person = res[0]
#         assert_that(person.id, equal_to("1"))
#         assert_that(person.name, equal_to("Nicolette Champlin"))

#     @it
#     def parse_a_person_with_1_appointment():
#         file = io.StringIO(
#             '''1;Nicolette Champlin
# 1;1/8/2015 11:30:00 AM;1/8/2015 2:00:00 PM;ABC'''
#             )

#         res = file_parser.parse(file)
#         person = res[0]
#         assert_that(person.appointments, has_length(1))


#     @it
#     def parse_appointment():
#         appointment_string = "1;1/8/2015 11:30:00 AM;1/8/2015 2:00:00 PM;ABC"
#         id, start, end = file_parser.parse_appointment(appointment_string)

#         assert_that(id, equal_to("1"))
#         assert_that(start, equal_to("1/8/2015 11:30:00 AM"))

