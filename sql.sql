Por supuesto, aquí están los mismos comandos SQL con ejemplos en español:

1. **SELECT**: Para recuperar datos de una tabla.

   ```sql
   SELECT * FROM empleados;
   ```

2. **INSERT**: Para agregar nuevos registros a una tabla.

   ```sql
   INSERT INTO empleados (id_empleado, nombre, apellido) VALUES (101, 'Juan', 'Pérez');
   ```

3. **UPDATE**: Para modificar registros existentes en una tabla.

   ```sql
   UPDATE empleados SET salario = 50000 WHERE id_empleado = 101;
   ```

4. **DELETE**: Para eliminar registros de una tabla.

   ```sql
   DELETE FROM empleados WHERE id_empleado = 101;
   ```

5. **CREATE TABLE**: Para crear una nueva tabla.

   ```sql
   CREATE TABLE productos (
       id_producto NUMBER(5),
       nombre_producto VARCHAR2(50),
       precio NUMBER(10, 2)
   );
   ```

6. **ALTER TABLE**: Para modificar la estructura de una tabla existente, como agregar una columna.

   ```sql
   ALTER TABLE empleados ADD (fecha_contratacion DATE);
   ```

7. **DROP TABLE**: Para eliminar una tabla y todos sus datos.

   ```sql
   DROP TABLE productos;
   ```

8. **CREATE VIEW**: Para crear una vista que represente una consulta.

   ```sql
   CREATE VIEW empleados_altos_salarios AS
   SELECT * FROM empleados WHERE salario > 60000;
   ```

9. **CREATE INDEX**: Para crear un índice en una columna de una tabla.

   ```sql
   CREATE INDEX idx_apellido ON empleados(apellido);
   ```

10. **CREATE PROCEDURE**: Para crear un procedimiento almacenado.

    ```sql
    CREATE OR REPLACE PROCEDURE obtener_info_empleado (id_emp NUMBER) AS
    BEGIN
        SELECT * FROM empleados WHERE id_empleado = id_emp;
    END;
    ```

11. **GRANT y REVOKE**: Para otorgar o revocar permisos a usuarios.

    ```sql
    GRANT SELECT ON empleados TO usuario1;
    REVOKE SELECT ON empleados FROM usuario1;
    ```

12. **COMMIT y ROLLBACK**: Para confirmar o deshacer transacciones.

    ```sql
    COMMIT;
    ROLLBACK;
    ```

13. **EJECUCIÓN DE SCRIPTS**: Para ejecutar un script SQL desde un archivo.

    ```sql
    @mi_script.sql;
    ```

Para crear claves primarias (Primary Key) y claves foráneas (Foreign Key) en SQL, puedes utilizar los siguientes ejemplos. Asegúrate de que estos comandos sean compatibles con la base de datos específica que estás utilizando, ya que la sintaxis puede variar ligeramente según el sistema de gestión de bases de datos (por ejemplo, Oracle, MySQL, SQL Server, etc.).

#### Crear una Primary Key:

```sql
-- Crear una tabla con una clave primaria
CREATE TABLE estudiantes (
    id_estudiante INT PRIMARY KEY,
    nombre VARCHAR(50),
    edad INT
);
```

En el ejemplo anterior, se crea una tabla llamada "estudiantes" con una columna "id_estudiante" que se define como clave primaria. Esto garantiza que los valores en la columna "id_estudiante" sean únicos en cada fila de la tabla.

#### Crear una Foreign Key:

```sql
-- Crear una tabla para representar cursos
CREATE TABLE cursos (
    id_curso INT PRIMARY KEY,
    nombre_curso VARCHAR(50)
);

-- Crear una tabla para representar la inscripción de estudiantes en cursos
CREATE TABLE inscripciones (
    id_inscripcion INT PRIMARY KEY,
    id_estudiante INT,
    id_curso INT,
    FOREIGN KEY (id_estudiante) REFERENCES estudiantes(id_estudiante),
    FOREIGN KEY (id_curso) REFERENCES cursos(id_curso)
);
```

En el ejemplo anterior, se crean dos tablas: "cursos" y "inscripciones". La tabla "inscripciones" tiene dos columnas, "id_estudiante" y "id_curso", que se declaran como claves foráneas que hacen referencia a las columnas correspondientes en las tablas "estudiantes" y "cursos", respectivamente. Esto establece una relación entre las tablas y garantiza que los valores en las columnas "id_estudiante" e "id_curso" en la tabla "inscripciones" estén vinculados a valores válidos en las tablas "estudiantes" y "cursos".

Recuerda que, en algunos sistemas de gestión de bases de datos, puede ser necesario definir explícitamente las restricciones de integridad referencial, como ON DELETE o ON UPDATE, al crear claves foráneas para especificar cómo deben manejarse las acciones cuando se actualizan o eliminan registros en las tablas relacionadas.

Por supuesto, aquí tienes ejemplos de cómo usar las cláusulas `JOIN`, `LEFT JOIN` y `RIGHT JOIN` para combinar datos de dos tablas en SQL. Supongamos que tenemos dos tablas: "clientes" y "pedidos".

#### Tabla "clientes":

```sql
CREATE TABLE clientes (
    id_cliente INT PRIMARY KEY,
    nombre_cliente VARCHAR(50)
);

INSERT INTO clientes (id_cliente, nombre_cliente)
VALUES
    (1, 'Juan'),
    (2, 'María'),
    (3, 'Pedro');
```

#### Tabla "pedidos":

```sql
CREATE TABLE pedidos (
    id_pedido INT PRIMARY KEY,
    id_cliente INT,
    producto VARCHAR(50)
);

INSERT INTO pedidos (id_pedido, id_cliente, producto)
VALUES
    (101, 1, 'Producto A'),
    (102, 1, 'Producto B'),
    (103, 2, 'Producto C'),
    (104, 3, 'Producto D');
```

Ahora, veamos ejemplos de cómo realizar diferentes tipos de JOIN entre estas dos tablas:

#### INNER JOIN (JOIN):

```sql
SELECT clientes.nombre_cliente, pedidos.producto
FROM clientes
INNER JOIN pedidos ON clientes.id_cliente = pedidos.id_cliente;
```

En este ejemplo, se realiza un INNER JOIN entre las tablas "clientes" y "pedidos" usando la columna "id_cliente" como el campo de unión. Esto devuelve solo los registros donde hay coincidencias en ambas tablas.

#### LEFT JOIN:

```sql
SELECT clientes.nombre_cliente, pedidos.producto
FROM clientes
LEFT JOIN pedidos ON clientes.id_cliente = pedidos.id_cliente;
```

Con un LEFT JOIN, se obtienen todos los registros de la tabla izquierda ("clientes") y los registros coincidentes de la tabla derecha ("pedidos"). Si no hay coincidencias en la tabla derecha, los valores serán NULL en la columna "producto".

#### RIGHT JOIN:

```sql
SELECT clientes.nombre_cliente, pedidos.producto
FROM clientes
RIGHT JOIN pedidos ON clientes.id_cliente = pedidos.id_cliente;
```

Con un RIGHT JOIN, obtienes todos los registros de la tabla derecha ("pedidos") y los registros coincidentes de la tabla izquierda ("clientes"). Si no hay coincidencias en la tabla izquierda, los valores serán NULL en la columna "nombre_cliente".

Estos son ejemplos de cómo utilizar JOIN, LEFT JOIN y RIGHT JOIN para combinar datos de dos tablas en SQL. El tipo de JOIN que elijas depende de la información que desees recuperar y cómo deseas manejar las coincidencias y no coincidencias entre las tablas.