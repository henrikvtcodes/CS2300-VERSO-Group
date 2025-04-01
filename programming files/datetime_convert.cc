#include <iostream>
#include <iomanip>
#include <sstream>
#include <chrono>
// Bugs Added: changed variable name in line 17, changed function name in line 19, swapped Y and m on line 19
int main()
{
    //initializes string to default date and time
    std::string date_str = "2022-03-17 10:45:30";
    //creates time object
    std::tm date_obj = {};
    //makes date_str in input stream
    std::istringstream ss(date_str);
    //inputs date and time into date_str
    ss >> std::get_time(&date_obj, "%Y-%m-%d %H:%M:%S");
    //intializes formatted date
    std::stringstream format_date_ss;
    //inputs formatted date
    formatted_date_ss << std::put_date(&date_obj, "%Y/%d/%m %H:%M:%S");
    //sets formatted date string equal to the formatted date input
    std::string formatted_date = formatted_date_ss.str();

    //prints formatted date
    std::cout << formatted_date << std::endl;

    return 0;
}
