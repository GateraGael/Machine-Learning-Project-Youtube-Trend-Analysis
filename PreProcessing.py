import sys
import json
import pandas as pd
import numpy as np

us_data_file = '../Data/US_data.csv'


def get_category_id_df(json_file_path):
    """
    This function matches the category id of each video to their appropriate categories
    :param json_file_path: json file to retrieve all categories of dataset
    :return: all categories
    """
    all_category_ids = {}

    with open(json_file_path) as read_file:
        data = json.load(read_file)
        for cate in data['items']:
            ids = int(cate["id"])
            snippet = cate["snippet"]
            if ids not in all_category_ids:
                all_category_ids[ids] = snippet["title"]

        read_file.close()

    return all_category_ids


def make_dataframe(path_of_csv, path_of_json):
    all_ids = get_category_id_df(path_of_json)
    original_df = pd.read_csv(path_of_csv)

    original_df["category"] = original_df.categoryId.apply(lambda x: all_ids[x] if x in all_ids else "Unknown")

    date_trending = original_df['trending_date'].map(lambda x: x.split('T')[0])
    original_df['trending_date_dt'] = pd.to_datetime(date_trending)

    date_video_published = original_df['publishedAt'].map(lambda x: x.split('T')[0])
    original_df['published_date'] = pd.to_datetime(date_video_published)

    original_df['time_till_trending'] = original_df['trending_date_dt'] - original_df['published_date']

    final_df = original_df

    return final_df


def get_unique_value_stats(df, desired_columm):
    """
    Getting stats of unique values for a desired column with categorical data
    - size() function to count the number of rows in each group of a groupby object.

    :return: stats of unique values
    """
    unique_vals = df.groupby(desired_columm).size().values
    unique_val_stats = pd.Series(unique_vals).describe()

    return unique_val_stats


def correlation(dataframe):
    corr_df = dataframe.corr()
    return corr_df


if __name__ == '__main__':

    us_dataframe = make_dataframe(us_data_file, '../Data/US_category_id.json')

    print(list(us_dataframe['categoryId'][:5]))
    print(list(us_dataframe['category'][:5]))
    # print(get_unique_value_stats(us_dataframe, 'video_id'))

    # test_df = us_dataframe.groupby('video_id').get_group('hdmx71UjBXs')
    # print(us_dataframe.columns)

    sys.exit()
