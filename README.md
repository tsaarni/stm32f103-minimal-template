# Minimal Mbed OS project template for barebones STM32F103

This is a template for a barebones STM32F103C8 project.

The project uses Mbed OS which is not optimized for memory footprint. With newlib-nano,
a small footprint variant of C standard library,
there is plenty of flash memory left for the application.

The development environment is based on PlatformIO.


## Connecting ST-LINK/V2 to STM32F103C8

Minimum connections for flashing are depicted below

![Imgur](https://i.imgur.com/sSIP43a.png)


## Programming

Compile and flash

    pio run -t upload


View serial debug logs

    pio device monitor -b 115200


## Manuals

* [Datasheet](https://www.st.com/resource/en/datasheet/cd00161566.pdf)
* AN2587 [Getting started with STM32F10xxx hardware development](https://www.st.com/content/ccc/resource/technical/document/application_note/6c/a3/24/49/a5/d4/4a/db/CD00164185.pdf/files/CD00164185.pdf/jcr:content/translations/en.CD00164185.pdf)
* RM0008 [Reference Manual](https://www.st.com/content/ccc/resource/technical/document/reference_manual/59/b9/ba/7f/11/af/43/d5/CD00171190.pdf/files/CD00171190.pdf/jcr:content/translations/en.CD00171190.pdf)
* [Mbed OS Documentation](https://os.mbed.com/docs/)
