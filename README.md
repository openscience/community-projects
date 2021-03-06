
## Folder structure
Collected information on projects can be found in the `/projects` folder in the root directory. A separate folder is assigned to each project. The folder name of a project must be unique within the collection and all spaces must be replaced by underscore (e.g. `example_project_name`).
```
/projects
   /{project_name}
      _meta.json          ← Project description 
      icon.svg            ← Project logo
```
**Obligatory**
- Every project directory must contain a `_meta.json` file, in which all meta data is stored in a uniform format.

**Optional**
- ICON: If a project can be associated with a logo, it is saved in `icon.svg`.

<br><br>
## Metadata structure
```
{
  "name": <string>,                     ← Project Name
  "desc": <multilang>,                  ← Project Description [...] >= 1
  "tags": [<string_lang>],              ← Project Search Tags
  "page": null OR <string>,             ← Project Website URL
  "socl": [] OR [<string>],             ← Projects social accounts, List of URL's
  "cmcl": null OR bool,                 ← Whether or not this project is commercial
  "founded": null OR <unix-time>,       ← Date of project creation
  "ceased": null OR <unix-time>,        ← Date of project termination
  "edit": <unix-time>,                  ← Last edit date UTC format as UNIX timestamp
}
```


```
// STRING_LANG
// An object that contains a string (text) and indicates the language used.
{
  "lng": <string>,                      ← ISO 639-2/T
  "txt": <string>,                      ← text
}

// MULTILANG
// A slice of 'STRING_LANG' objects; Each language indicator must be unique within a list.
[<STRING_LANG>...]

IDEA:
{
  "txt": <string>,
  "lng": <string>,
  "int": <multilang>,   ← translations
}
```
