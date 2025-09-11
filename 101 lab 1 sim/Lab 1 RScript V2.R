# STEP ONE:   read the "BIOSCI 101: Intro to R" instructions found in the lab 1 
#             CANVAS page
# STEP TWO:   put your data into lines 44 - 48, as shown in the "BIOSCI 101: 
#             Intro to R" instructions.
#             You do not need to change anything else in this R Script! 
# STEP THREE: Run this R Script from top to bottom. 
#             Run line by line by putting the cursor anywhere in line 1 without 
#             highlighting any text, then pressing "Run" from the top right-hand 
#             corner of this pane, or alternatively pressing "Ctrl + Enter"
#             successively for each line of code until you reach the end of the 
#             code.

# Read these green comments as you go along to help you semi-understand what is
# happening (if you have no coding experience). We will teach you more about this 
# when you take BIOSCI 220 next year! :-)

################################################################################
#####                         LOADING PACKAGES                              ####
################################################################################

# the install.packages lines below only needs to be run ONCE. Add a hash tag to
# the beginning of the lines once you've done this to make it turn into a green
# comment like this one! (R then does not evaluate it as code to run)
install.packages("tidyverse")
install.packages("Matrix", type = "binary")
install.packages("ggpmisc") # this can take approx. 1-2 mins to complete
library(tidyverse)
library(Matrix)
library(ggpmisc)


################################################################################
#####                  GETTING YOUR DATA INTO RSTUDIO                       ####
################################################################################

# to get your lab data into RStudio, input YOUR DATA in the empty brackets below 
# to create a data frame
# what is a data frame? A data frame is data stored in a table format

# it is important you type this in the correct order from your written data table
# i.e., read from top to bottom of each column to put data into each line below
# ask your TA's if you are uncertain :-)
group_member <- c("A", "B", "C", "D")
percent_dye <- c(10, 5, 1, 0.1)
expected <- c(, , , )
reading1 <- c(0.447, 0.243, 0.033, 0.045)
reading2 <- c([0.450, 0.242, 0.04, 0.03])
reading3 <- c(0.449, 0.238, 0.037, 0.035)

df <- data.frame(group_member, percent_dye, expected, reading1, reading2, reading3)
# if you'd like to check your data is accurately entered, run the code below
# so you can visualise the data in a table in the RStudio console
df


################################################################################
#####           CALCULATING THE MEAN AND STANDARD DEVIATION                 ####
################################################################################

# before R can calculate these summary statistics for us, we need to manipulate
# our data frame. R can easily do this for us (you do not need to do anything
# here but run the code!).
df_long <- df %>% 
  pivot_longer(cols = c("reading1", "reading2", "reading3"), names_to = "reading", values_to = "Absorbance")
# to see what this has done, print it to the console
df_long

# now R can easily calculate out what we want to know (the mean and standard deviation)
sum_stats <- df_long %>% 
  group_by(group_member) %>% 
  summarise(mean = mean(Absorbance), sd = sd(Absorbance))
# to see what this has done, print it to the console
sum_stats


################################################################################
#####                PRODUCING OUR PLOT WITH R^2 VALUE                      ####
################################################################################

# the code below will give us our plot (again, you do not need to do anything
# here but run the code!)

ggplot(data = sum_stats, aes(x = percent_dye, y = mean)) +
  # add on linear regression line
  geom_smooth(method = "lm", color="black", formula = y ~ x, se=FALSE) +
  # add R-squared value to plot
  stat_poly_eq() + 
  # add mean data points onto plot
  geom_point(shape = 18) +
  # add the reading data points for each group member onto plot
  geom_point(data = df_long, aes(x = percent_dye, y = Absorbance), shape = 4) +
  # add error bars onto plot
  geom_errorbar(aes(ymin = mean - sd, ymax  =mean + sd), width = .1) +
  theme_classic() +
  # specifying the x and y label and figure caption content
  labs(x = "% Dye", y = "Absorbance (@422 nm)", 
       caption = paste0(str_wrap("Figure 1: The spectrophotometric absorbance (@422nm) of yellow dye at varying concentrations (%). \u2715 indicates actual readings (n = 3), \U25C6 indicates the mean (average) of these three readings, error bars are standard deviation plotted around the mean value at each concentration"))) +
  # positioning the figure caption and changing the font size
  theme(plot.caption.position = "plot",
        plot.caption = element_text(hjust = 0.5, size = 12))


################################################################################
#####           DO YOU WANT TO SAVE YOUR PLOT? HERE'S HOW...                ####
################################################################################

# above plot window, click on "Export", then from dropdown choose "Save as Image"
# to save your plot if you want. You could send it to yourself via email to keep 
# it :-)

# You may also like to save this RScript somewhere (again, you could email it to 
# yourself) so you can revisit it in the future if you do anymore R coding.