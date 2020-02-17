"""There were about 116,990 polling places in the US for the 2016 election 
([source](https://www.eac.gov/documents/2017/11/15/eavs-deep-dive-poll-workers-and-polling-places)). 
This is to count of the nearly 139 million votes that were cast in the presidential race 
([source](https://www.businessinsider.com/trump-voter-turnout-records-history-obama-clinton-2016-11)). 
So that's about 1200 votes per polling place. Say you split that into four groups to count up the votes. 
At 5 seconds a count that 25 minutes to count up all the votes."""


def calc_time_at_polling_place(votes_per_polling_place, num_groups_counting_votes, seconds_to_count_vote):
    return (votes_per_polling_place / num_groups_counting_votes) * seconds_to_count_vote


def calc_time_at_tallying_office(seconds_to_report_results, num_places_reporting, seconds_to_sum_result):
    """This can be used at the district, regional, and state level
    """
    seconds_to_gather_results = seconds_to_report_results * num_places_reporting
    seconds_to_tally_results = num_places_reporting * seconds_to_sum_result
    return seconds_to_gather_results + seconds_to_tally_results


def calc_total_time(votes_per_polling_place, num_groups_counting_votes, time_to_count_vote):
    calc_time_at_polling_place(votes_per_polling_place, num_groups_counting_votes, seconds_to_count_vote) + \
        calc_time_at_tallying_office(seconds_to_report_results, )


votes_per_polling_place = 1200
num_groups_counting_votes = 4
seconds_to_count_vote = 5
seconds_to_sum_result = 5
seconds_to_report_results = 40 # time to connect with higher level voter office and report results



if __name__ == "__main__":
    calc_total_time(votes_per_polling_place=votes_per_polling_place)