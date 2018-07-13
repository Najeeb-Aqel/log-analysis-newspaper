#!/usr/bin/env python2.7
import psycopg2

query1 = ("select articles.title, count(*) as views from articles "
          "inner join log on log.path like concat('%',articles.slug,'%') "
          "where log.status='200 OK' group by articles.title order "
          "by views desc limit 3;")


query2 = ("select authors.name, count(*) as "
          "views from log,authors,articles where "
          "log.path like concat('%',articles.slug,'%') "
          "and articles.author=authors.id and "
          "log.status='200 OK' group by authors.name order by views desc;")

query3 = ("select fordate, perc from percentageB where perc>1;")


def printquery1(results):
    print "The most popular three articles of all time are:"
    for i, result in enumerate(results):
        print ("-" + result[0] + "--" + str(result[1]) + "views")
    print ("\n")


def printquery2(results):

    print "The most popular article authors of all time are:"
    for i, result in enumerate(results):
        print ("-" + result[0] + "--" + str(result[1]) + "views")
    print ("\n")


def printquery3(results):
    print "The days where more than 1% of requests led to errors:"
    for i, result in enumerate(results):
        print (str(result[0]) + "\t" + str(result[1]) + "%")
    print ("\n")


if __name__ == '__main__':
    conn = psycopg2.connect("dbname=news")
    cursor = conn.cursor()

    # executing and printing the result of quey 1
    cursor.execute(query1)
    results = cursor.fetchall()
    printquery1(results)

    # executing and printing the result of quey 2
    cursor.execute(query2)
    results = cursor.fetchall()
    printquery2(results)

    # executing and printing the result of quey 3
    cursor.execute(query3)
    results = cursor.fetchall()
    printquery3(results)

    conn.close()
