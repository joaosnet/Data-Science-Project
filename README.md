# Projeto Airbnb Rio - Property Price Prediction Tool for Ordinary People

## Context

In Airbnb, anyone who has a room or any type of property (apartment, house, chalet, inn, etc.) can offer their property for rent on a daily basis.

You create your host profile (person who makes a property available for daily rent) and create the listing for your property.

In this listing, the host must describe the property's characteristics as thoroughly as possible, in order to help renters/travelers choose the best property for them (and to make their listing more attractive).

There are numerous customizations available for your listing, ranging from minimum stay requirements, price, number of rooms, to cancellation policies, extra fees for additional guests, identity verification requirements for renters, etc.

## Screenshots

### Screenshot 1: Property Map View

![Property Map View](/screenshots/Property Map View.png)

_Figure 1: Property Map View_

## Our Goal

To build a price prediction model that allows an ordinary person who owns a property to determine how much they should charge for the daily rent of their property.

Alternatively, for the ordinary renter, given the property they are looking for, to help them determine if that property is competitively priced (below the average for properties with the same characteristics) or not.

## Available Data, Inspirations, and Credits

The datasets were obtained from the Kaggle website: [link](https://www.kaggle.com/allanbruno/airbnb-rio-de-janeiro)

They are available for download below the class (if you pull the data directly from Kaggle, you may find different results from mine, as the datasets may have been updated).

If you prefer an alternative solution, we can refer to the solution provided by Kaggle user Allan Bruno in the following notebook: [link](https://www.kaggle.com/allanbruno/helping-regular-people-price-listings-on-airbnb)

You will notice similarities between the solution we will develop here and his, but also some significant differences in the project construction process.

- The datasets contain property prices and their respective characteristics for each month.
- The prices are given in Brazilian Real (R$).
- We have data from April 2018 to May 2020, with the exception of June 2018, for which there is no dataset available.

## Initial Expectations

- I believe seasonality can be an important factor, as months like December tend to be expensive in Rio de Janeiro.
- The location of the property should make a significant difference in the price, as in Rio de Janeiro, the location can completely change the characteristics of the place (safety, natural beauty, tourist attractions).
- Additional amenities can have a significant impact, considering there are many old buildings and houses in Rio de Janeiro.

Let's explore how much these factors impact the prices and if there are other less intuitive factors that are extremely important.

```bash
pip install -r requirements.txt
