var DateUtil = {}

/**
 * Get verbose month name by index
 *
 * @param index
 * @param format
 * @returns {*|string}
 */
DateUtil.getMonthName = function(index, format){
    short_month_index = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
    full_month_index = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
                        'September', 'October', 'November', 'December'];

    if (!format){
        format='short';
    }
    if (format=='full'){
        return full_month_index[index];
    }
    return short_month_index[index];
}

/**
 * Get verbose week day name by index
 *
 * @param index
 * @param format
 * @returns {*|string}
 */
DateUtil.getWeekdayName = function(index, format){
    short_weekname_index = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'];
    full_weekname_index = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'];

    if (!format){
        format='short';
    }
    if (format=='full'){
        return full_weekname_index[index];
    }
    return short_weekname_index[index];
}

/**
 * Calculate the difference in days between two dates
 *
 * @param start_date
 * @param end_date
 * @returns {number|*}
 */
DateUtil.getDayDifference = function(start_date, end_date){
    // @todo function input validation
    num_days = Math.floor(
        (
            Date.UTC(end_date.getFullYear(), end_date.getMonth(), end_date.getDate()) -
            Date.UTC(start_date.getFullYear(), start_date.getMonth(), start_date.getDate()) )
        /
        (1000 * 60 * 60 * 24));
    return num_days;
}