
`@property` - сеттер может работать автоматически во время инициализации, если атрибут назван без `__`;
`@property` магическим образом переименовывает атрибут в защищённый на момент инициализации, хотя его сеттер не срабатывает в это время(если атрибут назван с `__`);
Магический `__setattr__` автоматически срабатывает во время инициализации;
`@property` вместе с `__setattr__` работают в следующем порядке: вызываем атрибут -> `__setattr__`(атрибут) -> `@property`(__атрибут) -> `__setattr__(__атрибут)` -> доступ к __атрибуту получен
Дескриптор работает так же и в таком же порядке, как и `@property`, но у `@property` больший приоритет, поэтому, если запустить сразу оба, то Дескриптор не будет срабатывать.
