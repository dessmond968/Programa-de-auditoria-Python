# Sistema de Auditoría de Inventario

## Descripción

Este proyecto consiste en una aplicación desarrollada en **Python** con interfaz gráfica utilizando la librería **Tkinter**, diseñada para auditar el inventario de una empresa y determinar de forma automática qué artículos requieren ser reabastecidos.

El programa trabaja con una matriz que almacena la información de cada producto, incluyendo el código, el nombre del artículo, el stock actual y el stock mínimo requerido. Mediante una función específica, compara el inventario disponible con el nivel mínimo establecido y calcula la cantidad exacta de unidades que deben solicitarse para cada artículo.

La aplicación presenta los resultados en una interfaz gráfica intuitiva mediante una tabla donde se muestran el código del producto, el nombre, el stock actual, el stock mínimo, la cantidad que debe solicitarse y el estado del inventario, indicando si el artículo requiere reabastecimiento o si cuenta con existencias suficientes.

Además, el sistema genera un resumen con el número total de artículos analizados, la cantidad de productos que necesitan reposición y el total de unidades que deben solicitarse, facilitando el control del inventario y apoyando la toma de decisiones.

## Características principales

* Interfaz gráfica desarrollada con **Tkinter** y **ttk**.
* Gestión del inventario mediante una matriz de datos.
* Función modular para calcular la cantidad de reabastecimiento.
* Auditoría automática de todos los artículos del inventario.
* Tabla con información organizada y estado de cada producto.
* Resumen estadístico del inventario auditado.
* Código estructurado en funciones, siguiendo buenas prácticas de programación y facilitando su mantenimiento.

## Tecnologías utilizadas

* Python 3
* Tkinter
* ttk (Themed Tkinter Widgets)

## Objetivo

El objetivo de este proyecto es demostrar la aplicación de estructuras de datos, funciones, ciclos e interfaces gráficas en Python para resolver un problema de gestión de inventarios, permitiendo identificar de forma rápida y precisa los artículos que deben ser reabastecidos.
