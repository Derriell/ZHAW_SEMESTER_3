#include "utils_ctboard.h"
#include "cdBoardAdresses.h"
#include "displayPattern.h"

const uint_fast8_t leastSignificantFourBits = 0x0F;

int main (){
    while(1){
        write_word(LEDS, read_word(SWITCHES));
        
        uint16_t rotaryValue = read_byte(ROTARY_P11) & leastSignificantFourBits;
        
        write_byte(DISPLAY_DS0, DISPLAY_PATTERNS[rotaryValue]);
    }
} 