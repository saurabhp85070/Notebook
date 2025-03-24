# Databricks notebook source
# MAGIC
# MAGIC %md-sandbox
# MAGIC
# MAGIC <div style="text-align: center; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning" style="width: 600px">
# MAGIC </div>

# COMMAND ----------

# MAGIC %md
# MAGIC # Data Science Project
# MAGIC
# MAGIC **Objective**: *Design, complete, and assess a common data science project.*
# MAGIC
# MAGIC In this lab, you will use the data science process to design, build, and assess a common data science project.

# COMMAND ----------

# MAGIC %run "../../Includes/Classroom-Setup"

# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC ## Project Details
# MAGIC
# MAGIC In recent months, our health tracker company has noticed that many customers drop out of the sign-up process when they have to self-identify their exercise lifestyle (`ht_users.lifestyle`) – this is especially true for those with a "Sedentary" lifestyle. As a result, the company is considering removing this step from the sign-up process. However, the company knows this data is valuable for targeting introductory exercises and they don't want to lose it for customers that sign up after the step is removed.
# MAGIC
# MAGIC In this data science project, our business stakeholders are interested in identifying which customers have a sedentary lifestyle – specifically, they want to know if we can correctly identify whether somebody has a "Sedentary" lifestyle at least 95 percent of the time. If we can meet this objective, the organization will be able to remove the lifestyle-specification step of the sign-up process *without losing the valuable information provided by the data*.
# MAGIC
# MAGIC
# MAGIC <img alt="Side Note" title="Side Note" style="vertical-align: text-bottom; position: relative; height:1.75em; top:0.05em; transform:rotate(15deg)" src="https://files.training.databricks.com/static/images/icon-note.webp"/> There are no solutions provided for this project. You will need to complete it independently using the guidance detailed below and the previous labs from the project.

# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC
# MAGIC ## Exercise 1
# MAGIC
# MAGIC Summary: 
# MAGIC * Specify the data science process question. 
# MAGIC * Indicate whether this is framed as a supervised learning or unsupervised learning problem. 
# MAGIC * If it is supervised learning, indicate whether the problem is a regression problem or a classification problem.
# MAGIC
# MAGIC <img alt="Hint" title="Hint" style="vertical-align: text-bottom; position: relative; height:1.75em; top:0.3em" src="https://files.training.databricks.com/static/images/icon-light-bulb.svg"/>&nbsp;**Hint:** When we are interested in predicting something, we are usually talking about a supervised learning problem.

# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC
# MAGIC ## Exercise 2
# MAGIC
# MAGIC Summary: 
# MAGIC
# MAGIC * Specify the data science objective. 
# MAGIC * Indicate which evaluation metric should be used to assess the objective.
# MAGIC
# MAGIC <img alt="Hint" title="Hint" style="vertical-align: text-bottom; position: relative; height:1.75em; top:0.3em" src="https://files.training.databricks.com/static/images/icon-light-bulb.svg"/>&nbsp;**Hint:** Remember, the data science objective needs to be measurable.

# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC
# MAGIC ## Exercise 3
# MAGIC
# MAGIC Summary:
# MAGIC * Design a baseline solution.
# MAGIC * Develop a baseline solution – be sure to split data between training for development and test for assessment.
# MAGIC * Assess your baseline solution. Does it meet the project objective? If not, use it as a threshold for further development.
# MAGIC
# MAGIC <img alt="Hint" title="Hint" style="vertical-align: text-bottom; position: relative; height:1.75em; top:0.3em" src="https://files.training.databricks.com/static/images/icon-light-bulb.svg"/>&nbsp;**Hint:** Recall that baseline solutions are meant to be easy to develop.

# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC
# MAGIC ## Exercise 4
# MAGIC
# MAGIC Summary: 
# MAGIC * Design the machine learning solution, but do not yet develop it. 
# MAGIC * Indicate whether a machine learning model will be used. If so, indicate which machine learning model will be used and what the label/output variable will be.
# MAGIC
# MAGIC <img alt="Hint" title="Hint" style="vertical-align: text-bottom; position: relative; height:1.75em; top:0.3em" src="https://files.training.databricks.com/static/images/icon-light-bulb.svg"/>&nbsp;**Hint:** Consider solutions that align with the framing you did in Exercise 1.

# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC ## Exercise 5
# MAGIC
# MAGIC Summary: 
# MAGIC * Explore your data. 
# MAGIC * Specify which tables and columns will be used for your label/output variable and your feature variables.
# MAGIC
# MAGIC <img alt="Hint" title="Hint" style="vertical-align: text-bottom; position: relative; height:1.75em; top:0.3em" src="https://files.training.databricks.com/static/images/icon-light-bulb.svg"/>&nbsp;**Hint:** Consider aggregating features from other tables.

# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC ## Exercise 6
# MAGIC
# MAGIC Summary: 
# MAGIC * Prepare your modeling data. 
# MAGIC * Create a customer-level modeling table with the correct output variable and features. 
# MAGIC * Finally, split your data between training and test sets. Make sure this split aligns with that of your baseline solution.
# MAGIC
# MAGIC <img alt="Hint" title="Hint" style="vertical-align: text-bottom; position: relative; height:1.75em; top:0.3em" src="https://files.training.databricks.com/static/images/icon-light-bulb.svg"/>&nbsp;**Hint:** Consider how to make the data split reproducible.

# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC ## Exercise 7
# MAGIC
# MAGIC Summary: 
# MAGIC * Build the model specified in your answer to Exercise 4. 
# MAGIC * Be sure to use an evaluation metric that aligns with your specified objective.
# MAGIC
# MAGIC <img alt="Hint" title="Hint" style="vertical-align: text-bottom; position: relative; height:1.75em; top:0.3em" src="https://files.training.databricks.com/static/images/icon-light-bulb.svg"/>&nbsp;**Hint:** This evaluation metric should align with the one used in your baseline solution.

# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC ## Exercise 8
# MAGIC
# MAGIC Summary: 
# MAGIC * Assess your model against the overall objective. 
# MAGIC * Be sure to use an evaluation metric that aligns with your specified objective.
# MAGIC
# MAGIC <img alt="Hint" title="Hint" style="vertical-align: text-bottom; position: relative; height:1.75em; top:0.3em" src="https://files.training.databricks.com/static/images/icon-light-bulb.svg"/>&nbsp;**Hint:** Remember that we assess our models against our test data set to ensure that our solutions generalize.
# MAGIC
# MAGIC <img alt="Hint" title="Hint" style="vertical-align: text-bottom; position: relative; height:1.75em; top:0.3em" src="https://files.training.databricks.com/static/images/icon-light-bulb.svg"/>&nbsp;**Hint:** If your solution doesn't meet the objective, consider tweaking the model and data used by the model until it does meet the objective.

# COMMAND ----------

# MAGIC %md
# MAGIC After completing all of the above objectives, you should be ready to communicate your results. Move to the next video in the lesson for a description on that part of the project.
# MAGIC

# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC &copy; 2021 Databricks, Inc. All rights reserved.<br/>
# MAGIC Apache, Apache Spark, Spark and the Spark logo are trademarks of the <a href="http://www.apache.org/">Apache Software Foundation</a>.<br/>
# MAGIC <br/>
# MAGIC <a href="https://databricks.com/privacy-policy">Privacy Policy</a> | <a href="https://databricks.com/terms-of-use">Terms of Use</a> | <a href="http://help.databricks.com/">Support</a>