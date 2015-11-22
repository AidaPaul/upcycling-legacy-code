# Created by Tymoteusz Paul at 22/11/2015
Feature: Checking credentials for given mailboxes
  We need to make sure that given credentials the app works as expected as so
  far we were relying on, based on nothing, notion that it just works.

  Scenario Outline: Valid credentials
    Examples:
      | username, password, host, port |

  Scenario Outline: Invalid credentials
    Examples:
      | username, password, host, port |
