/* -----------------------------------------------------------------
 * --  _____       ______  _____                                    -
 * -- |_   _|     |  ____|/ ____|                                   -
 * --   | |  _ __ | |__  | (___    Institute of Embedded Systems    -
 * --   | | | '_ \|  __|  \___ \   Zurich University of             -
 * --  _| |_| | | | |____ ____) |  Applied Sciences                 -
 * -- |_____|_| |_|______|_____/   8401 Winterthur, Switzerland     -
 * ------------------------------------------------------------------
 * --
 * -- main.c
 * --
 * -- main for Computer Engineering "Bit Manipulations"
 * --
 * -- $Id: main.c 744 2014-09-24 07:48:46Z ruan $
 * ------------------------------------------------------------------
 */
// #include <reg_ctboard.h>
#include "utils_ctboard.h"

#define ADDR_DIP_SWITCH_31_0 0x60000200
#define ADDR_DIP_SWITCH_7_0 0x60000200
#define ADDR_LED_31_24 0x60000103
#define ADDR_LED_23_16 0x60000102
#define ADDR_LED_15_8 0x60000101
#define ADDR_LED_7_0 0x60000100
#define ADDR_BUTTONS 0x60000210

// define your own macros for bitmasks below (#define)
/// STUDENTS: To be programmed

#define LED_6_7_MASK_ALWAYS_ON 0b11000000
#define LED_4_5_MASK_ALWAYS_OFF 0b11001111
#define BUTTON_MASK 0b00001111
#define T_0 0b00000001
#define T_1 0b00000010
#define T_2 0b00000100
#define T_3 0b00001000

/// END: To be programmed

int main(void)
{
    uint8_t led_value = 0;

    // add variables below
    /// STUDENTS: To be programmed
    uint8_t previousState = 0;
    uint8_t currentState = 0;
    uint8_t event;
    uint8_t counter = 0;
    uint8_t wrongCounter = 0;

    /// END: To be programmed

    while (1)
    {
        // ---------- Task 3.1 ----------
        led_value = read_byte(ADDR_DIP_SWITCH_7_0);

        /// STUDENTS: To be programmed

        // led 6-7 are set to 1
        led_value |= LED_6_7_MASK_ALWAYS_ON;

        led_value &= LED_4_5_MASK_ALWAYS_OFF;

        /// END: To be programmed

        write_byte(ADDR_LED_7_0, led_value);

        // ---------- Task 3.2 and 3.3 ----------
        /// STUDENTS: To be programmed
        previousState = currentState;
        currentState = read_byte(ADDR_BUTTONS) & BUTTON_MASK;
        event = previousState & ~currentState;

        if (currentState != 0)
        {
            wrongCounter++;
        }
        if (event & T_0)
        {
            counter++;
            write_byte(ADDR_LED_23_16,read_byte(ADDR_LED_23_16) / 2);
        }
        if (event & T_1)
        {
            write_byte(ADDR_LED_23_16,read_byte(ADDR_LED_23_16) * 2);
        }
        if (event & T_2)
        {
            write_byte(ADDR_LED_23_16,~read_byte(ADDR_LED_23_16));
        }
        if (event & T_3)
        {
            write_byte(ADDR_LED_23_16, read_byte(ADDR_DIP_SWITCH_7_0));
        }

        write_byte(ADDR_LED_15_8, wrongCounter);
        write_byte(ADDR_LED_31_24, counter);

        /// END: To be programmed
    }
}
