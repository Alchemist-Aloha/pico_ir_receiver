# IR Receiver for [Pico Light Bulbs Project](https://github.com/Alchemist-Aloha/rp2040_ws2812_led_controller)

This is the MicroPython code for the second Pico used to receive the IR signals and send them to the main Pico via UART. 

## Hardware

- **Raspberry Pi Pico**: Main microcontroller.
- **VS1838B IR Receiver**: For receiving signals from an infrared remote control.

## Project Structure

- **irrecvdata.py**: Manages communication with the LD2410 sensor.
- **main.py**: Main program that handle the ir receive and UART out.

## Usage

- **Buttons**:
  - Button 1: Increase brightness.
  - Button 2: Decrease brightness.
  - Button 3: Switch to human sensor mode.
  - Button 4: Toggle between always on and always off modes.

## License

This project is licensed under the MIT License.