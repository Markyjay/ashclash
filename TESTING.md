# Testing

[Click here to go back to the README.md file](README.md)

## Overview

This document outlines the testing process for the Sleep Healthily website. The testing process includes manual testing, performance testing and code validation. The testing process was carried out on Google Chrome, Mozilla Firefox, and Safari on MacBook.

## Table of Contents

- [Validation](#validation)
  - [HTML](#html)
  - [CSS](#css)
  - [JavaScript](#javascript)
  - [Python and Django (Pep 8)](#python-and-django-pep-8)
- [Performance](#performance)
  - [Mobile Performance](#mobile-performance)
  - [Desktop Performance](#desktop-performance)
- [Manual Testing](#manual-testing)
- [Incomplete known bugs and UX improvements](#incomplete-known-bugs-and-ux-improvements)

## Validation

### HTML

I use the [W3C Markup Validation Service](https://validator.w3.org/) to validate my HTML code.

With Django, there's a lot of syntax that doesn't play well with the HTML Validator, such as `{% url 'homepage' %}` or `{{ variable|filter }}`.

Normally, I validate by using [validate by uri](https://validator.w3.org/#validate_by_uri) by passing in my deployed URL. However, many pages on this site require a user to be logged in and authenticated, and will not work using this method, due to the fact that the HTML Validator (W3C) doesn't have access to login to the pages.

In order to properly validate my HTML pages for authenticated pages, I followed these steps:

- Navigate to the deployed pages that require authentication
- Right-click anywhere on the page, and select **View Page Source** (usually `CTRL+U` or `⌘+U` on Mac).
- This will display the entire compiled code.
- Copy everything, and use the [validate by input](https://validator.w3.org/#validate_by_input) method.
- Repeat this process for every page that requires a user to be logged-in/authenticated.

| Page             | W3C URL                                                                                                                                             | Screenshot                                                                         | Notes                                                                 |
| ---------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | --------------------------------------------------------------------- |
| Homepage         | [Link](https://validator.w3.org/....)                                                        | ![Homepage Validation](documentation/validation/html/homepage.png)                 | Pass                                                                  |
| About            | NA                                                                                                                                                  | ![About Validation](documentation/validation/html/about.png)                       | Pass                                                                  |
| Review Add         | NA                                                                                                                                                  | ![Blog Add Validation](documentation/validation/html/blog-add.png)                 | Errors are standard when using summernote on frontend                 |
| Review Edit        | NA                                                                                                                                                  | ![Blog Edit Validation](documentation/validation/html/blog-edit.png)               | Errors are standard when using summernote on frontend                 |
| Promotions | [Link](https://validator.w3.org/......)                                                  | ![Blog Post Detail Validation](documentation/validation/html/promotions.png) | Pass                                                                  |
| Promotion Add       | [Link](https://validator.w3.org/...)                                                   | ![Blog Posts Validation](documentation/validation/html/addpromotions.png)             | Pass                                                                  |
| Basket             | NA                                                                                                                                                  | ![Cart Validation](documentation/validation/html/basket.png)                         | Pass                                                                  |
| Checkout         | NA                                                                                                                                                  | ![Checkout Validation](documentation/validation/html/checkout.png)                 | Pass                                                                  |
| Contact          | [Link](https://validator.w3.org/.....)                                                | ![Contact Validation](documentation/validation/html/contact.png)                   | Pass                                                                  |
| Edit Product     | NA                                                                                                                                                  | ![Edit Product Validation](documentation/validation/html/edit-product.png)         | Duplicate error ID when using Custom Clearable input from CI Tutorial |
| Login            | [Link](https://validator.w3.org/.....)                                         | ![Login Validation](documentation/validation/html/login.png)                       | Pass                                                                  |
| Order Summary    | [Link](https://validator.w3.org/......) | ![Order Summary Validation](documentation/validation/html/order-summary.png)       | Scope error due to Bootstrap 4 syntax                                 |
| Product Detail   | [Link](https://validator.w3.org/......)                                 | ![Product Detail Validation](documentation/validation/html/product-detail.png)     | Pass                                                                  |
| Products         | [Link](https://validator.w3.org/.......)                                               | ![Products Validation](documentation/validation/html/products.png)                 | Pass                                                                  |
| Signup           | [Link](https://validator.w3.org/.......)                                        | ![Signup Validation](documentation/validation/html/signup.png)                     | Pass                                                                  |

### CSS

I use the [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) to validate my CSS code. You can [click here to see the validated CSS code without any errors](https://jigsaw.w3.org/css-validator/......).

### JavaScript

I used [JSHint](https://jshint.com/) to validate my JavaScript code. Here is a table of the validated code, which shows the file validated, a screenshot and a description of any warnings:

| File        | Screenshot                                                               | Description                                                                       |
| ----------- | ------------------------------------------------------------------------ | --------------------------------------------------------------------------------- |
| `script.js` | ![AshClash script](documentation/validation/js/jshint-script.png) | Optional chaining warning because online validator can't recognise I'm using ES11 |

### Python and Django (Pep 8)

I used the [Code Institute PEP8 Validator](https://pep8ci.herokuapp.com/) to check that my Python code is PEP8 compliant. I validated any files that were either modified or created by me. Here is a table of the validated code, which shows the file validated, a screenshot, and a description of any warnings:

| File                        | Screenshot                                                                              | Description                                                                                   |
| --------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| ashclash/settings.py | ![ashclash-settings](documentation/validation/pep8/ashclash-settings.png) | There are 4 errors that come from standard settings.py lines. It is advised not to edit them. |
| basket/contexts.py            | ![basket-contexts](documentation/validation/pep8/basket-contexts.png)                       | Pass                                                                                          |
| basket/admin.py               | ![basket-admin](documentation/validation/pep8/basket-admin.png)                             | Pass                                                                                          |
| basket/contexts.py            | ![basket-contexts](documentation/validation/pep8/basket-contexts.png)                       | Pass                                                                                          |
| basket/views.py               | ![basket-views](documentation/validation/pep8/basket-views.png)                               | Pass                                                                                          |
| basket/urls.py                | ![basket-urls](documentation/validation/pep8/basket-urls.png)                               | Pass                                                                                          |
| promotions/forms.py               | ![promotions-forms](documentation/validation/pep8/promotions-forms.png)                             | Pass                                                                                          |
| promotions/models.py              | ![promotions-models](documentation/validation/pep8/promotions-models.png)                           | Pass                                                                                          |
| promotions/urls.py                | ![promotions-urls](documentation/validation/pep8/promotions-urls.png)                               | Pass                                                                                          |
| promotions/views.py               | ![promotions-views](documentation/validation/pep8/promotions-views.png)                             | Pass                                                                                          |
| checkout/admin.py           | ![checkout-admin](documentation/validation/pep8/checkout-admin.png)                     | Pass                                                                                          |
| checkout/forms.py           | ![checkout-forms](documentation/validation/pep8/checkout-forms.png)                     | Pass                                                                                          |
| checkout/models.py          | ![checkout-models](documentation/validation/pep8/checkout-models.png)                   | Pass                                                                                          |
| checkout/signals.py         | ![checkout-signals](documentation/validation/pep8/checkout-signals.png)                 | Pass                                                                                          |
| checkout/urls.py            | ![checkout-urls](documentation/validation/pep8/checkout-urls.png)                       | Pass                                                                                          |
| checkout/views.py           | ![checkout-views](documentation/validation/pep8/checkout-views.png)                     | Pass                                                                                          |
| checkout/webhook_handler.py | ![checkout-webhook_handler](documentation/validation/pep8/checkout-webhook_handler.png) | Pass                                                                                          |
| checkout/webhooks.py        | ![checkout-webhooks](documentation/validation/pep8/checkout-webhooks.png)               | Pass                                                                                          |
| home/urls.py                | ![home-urls](documentation/validation/pep8/home-urls.png)                               | Pass                                                                                          |
| home/views.py               | ![home-views](documentation/validation/pep8/home-views.png)                             | Pass                                                                                          |
| product/admin.py            | ![product-admin](documentation/validation/pep8/product-admin.png)                       | Pass                                                                                          |
| product/forms.py            | ![product-forms](documentation/validation/pep8/product-forms.png)                       | Pass                                                                                          |
| product/helper_tags.py      | ![product-helper_tags](documentation/validation/pep8/product-helper_tags.png)           | Pass                                                                                          |
| product/models.py           | ![product-models](documentation/validation/pep8/product-models.png)                     | Pass                                                                                          |
| product/urls.py             | ![product-urls](documentation/validation/pep8/product-urls.png)                         | Pass                                                                                          |
| product/views.py            | ![product-views](documentation/validation/pep8/product-views.png)                       | Pass                                                                                          |
| product/widgets.py          | ![product-widgets](documentation/validation/pep8/product-widgets.png)                   | Pass                                                                                          |
| profiles/admin.py           | ![profiles-admin](documentation/validation/pep8/profiles-admin.png)                     | Pass                                                                                          |
| profiles/forms.py           | ![profiles-forms](documentation/validation/pep8/profiles-forms.png)                     | Pass                                                                                          |
| profiles/models.py          | ![profiles-models](documentation/validation/pep8/profiles-models.png)                   | Pass                                                                                          |
| profiles/urls.py            | ![profiles-urls](documentation/validation/pep8/profiles-urls.png)                       | Pass                                                                                          |
| profiles/views.py           | ![profiles-views](documentation/validation/pep8/profiles-views.png)                     | Pass                                                                                          |
| review/admin.py             | ![review-admin](documentation/validation/pep8/review-admin.png)                         | Pass                                                                                          |
| review/forms.py             | ![review-forms](documentation/validation/pep8/review-forms.png)                         | Pass                                                                                          |
| review/models.py            | ![review-models](documentation/validation/pep8/review-models.png)                       | Pass                                                                                          |
| review/urls.py              | ![review-urls](documentation/validation/pep8/review-urls.png)                           | Pass                                                                                          |
| review/views.py             | ![review-views](documentation/validation/pep8/review-views.png)                         | Pass                                                                                          |
| ashclash/urls.py     | ![ashclash-urls](documentation/validation/pep8/ashclash-urls.png)         | Pass                                                                                          |
| ashclash/views.py    | ![ashclash-views](documentation/validation/pep8/ashclash-views.png)       | Pass                                                                                          |

## Performance

Performance metrics were gathered using Google's PageSpeed Insights to ensure the website operates efficiently on both mobile and desktop devices. Below are the performance results with Lighthouse screenshots from the `documentation/performance` directory.

### Mobile Performance

| Page            | Lighthouse Screenshot                                                           | Comments                                                                                       |
| --------------- | ------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| Homepage        | ![Homepage Mobile](documentation/performance/mobile-homepage.png)               |                                                                                                |
| Login           | ![Login Mobile](documentation/performance/mobile-login.png)                     |                                                                                                |
| Order Summary   | ![Order Summary Mobile](documentation/performance/mobile-order-summary.png)     |                                                                                                |
| Product Detail  | ![Product Mobile](documentation/performance/mobile-product.png)                 |                                                                                                |
| Products        | ![Products Mobile](documentation/performance/mobile-products.png)               |                                                                                                |
| Search          | ![Search Mobile](documentation/performance/mobile-search.png)                   |                                                                                                |
| Signup          | ![Signup Mobile](documentation/performance/mobile-signup.png)                   |                                                                                                |

### Desktop Performance

| Page            | Lighthouse Screenshot                                                             | Comments       |
| --------------- | --------------------------------------------------------------------------------- | -------------- |
| Homepage        | ![Homepage Desktop](documentation/performance/desktop-homepage.png)               |                |
| Login           | ![Login Desktop](documentation/performance/desktop-login.png)                     |                |
| Order Summary   | ![Order Summary Desktop](documentation/performance/desktop-order-summary.png)     |                |
| Privacy Policy  | ![Privacy Policy Desktop](documentation/performance/desktop-privacy-policy.png)   |                |
| Product Detail  | ![Product Detail Desktop](documentation/performance/desktop-product-detail.png)   |                |
| Products        | ![Products Desktop](documentation/performance/desktop-products.png)               |                |
| Search          | ![Search Desktop](documentation/performance/desktop-search.png)                   |                |
| Shipping Policy | ![Shipping Policy Desktop](documentation/performance/desktop-shipping-policy.png) |                |
| Signup          | ![Signup Desktop](documentation/performance/desktop-signup.png)                   |                |

## Manual Testing

I carried out manual testing according to my user stories. To be considered a pass, it needs to have met the acceptance criteria. I carried the tests out on Google Chrome, Mozilla Firefox, and Safari on MacBook.

| User story - As an admin, I want to be able to...                                                                            | Notes  | Chrome | Firefox | Safari |
| ---------------------------------------------------------------------------------------------------------------------------- | ------ | :----: | :-----: | :----: |
| **monitor user profiles** to **maintain an accurate user database**.                                                         | Passed |   ✅   |   ✅   |   ✅   |
| **create new products** to **offer more choices to customers**.                                                              | Passed |   ✅   |   ✅   |   ✅   |
| **update product details** to **ensure all information about the products is current and accurate**.                         | Passed |   ✅   |   ✅   |   ✅   |
| **delete products** to **remove items that are no longer available or relevant**.                                            | Passed |   ✅   |   ✅   |   ✅   |
| **to view a list of all promotional player profiles** to **efficiently manage and monitor the product promotions**.          | Passed |   ✅   |   ✅   |   ✅   |
| **to add new player profiles** to **keep the player database current and complete**.                                         | Passed |   ✅   |   ✅   |   ✅   |
| **edit existing player profiles** to **update information as needed**.                                                       | Passed |   ✅   |   ✅   |   ✅   |
| **delete player profiles that are no longer active** to **to maintain a clean and updated player database**.                 | Passed |   ✅   |   ✅   |   ✅   |
| **monitor reviews left by customer** to **keep consider advice given by my consumers**.                                      | Passed |   ✅   |   ✅   |   ✅   |
| **delete reviews** to **keep them relevent and clean**.                                                                      | Passed |   ✅   |   ✅   |   ✅   |


| User story - As a user, I can...                                                                                             | Notes  | Chrome | Firefox | Safari |
| ---------------------------------------------------------------------------------------------------------------------------- | ------ | :----: | :-----: | :----: |
| **create an account** to **access personalised features and save my purchase history**.                                      | Passed |   ✅   |   ✅   |   ✅   |
| **log into my account** to **access my personal settings and order history, or prefill my details at checkout**.             | Passed |   ✅   |   ✅   |   ✅   |
| **log out of my account** to **ensure my account is secure when I'm not using it**.                                          | Passed |   ✅   |   ✅   |   ✅   |
| **access and view my user profile** to **see my personal information, order history, and manage my account settings**.       | Passed |   ✅   |   ✅   |   ✅   |
| **edit and delete my account** to **change or remove my personal data from the platform**.                                   | Passed |   ✅   |   ✅   |   ✅   |
| **search for products** to **find specific items I'm interested in purchasing**.                                             | Passed |   ✅   |   ✅   |   ✅   |
| **sort products by criteria** to **easily find what I'm looking for**.                                                       | Passed |   ✅   |   ✅   |   ✅   |
| **view product details** to **make informed purchase decision**.                                                             | Passed |   ✅   |   ✅   |   ✅   |
| **add products to my basket** to **purchase them**.                                                                          | Passed |   ✅   |   ✅   |   ✅   |
| **update or remove products from my basket** to **manage items before finalizing my purchase**.                              | Passed |   ✅   |   ✅   |   ✅   |
| **view a summary of my orders** to **keep track of my purchases**.                                                           | Passed |   ✅   |   ✅   |   ✅   |
| **complete the checkout process and pay** to **finalise my order**.                                                          | Passed |   ✅   |   ✅   |   ✅   |
| **create reviews for products** to **share my experience with others**.                                                      | Passed |   ✅   |   ✅   |   ✅   |
| **update my reviews** to **modify my feedback if my opinion changes**.                                                       | Passed |   ✅   |   ✅   |   ✅   |
| **delete my reviews** to **remove my feedback if I no longer wish it to be displayed**.                                      | Passed |   ✅   |   ✅   |   ✅   |



## Incomplete known bugs and UX improvements

The below are known bugs and possible areas of UX improvement I came across during testing.

1. 