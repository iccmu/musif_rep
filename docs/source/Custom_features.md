# Custom features

While using `musif`, you will be able to add your custom features.

There are 2 different types of features:
* basic features
* generic features

The only difference between them is that the “basic features” will be computed once for
each music score, while the “generic features” will be recomputed for each window in the
score. If you disable windows in the [configuration](./Config_extraction_example.html)
with the option `window_size: null`, then there will be no difference. However, the “basic
features” will always be computed before the “generic features”.

Each feature should have two functions:
* `update_part_objects`, which computes the features from each part in the score (or
  window)
* `update_score_objects`, which computes global calculations for the score (or window) or 
  for multiple parts (e.g. features for all the wind instruments or all the strings)

`update_part_objects` will be executed for each part on the score, unless that part is
not filtered out with `parts_filter` in the [configuration](Configuration.html).
Successively, `update_score_objects` is run once to include the final info in the
`score_features`. In this process, you can use the features computed at the part level
for computing features at the score level — for instance if you want to create a feature
only for the violins or for a certain family of instruments. Only the features at the
score level are inserted into the final DataFrame.

The two functions have similar signatures and contain the following:
* `score_data`: a dictionary containing all the data loaded from the score or from the
  cache; it contains `music21` objects representing score information and `pandas` DataFrames containing MuseScore harmonic annotations (if any feature containing harmonic data is requested).
  You may want to use this object to design your features. Remember that `music21` objects
  should **never** be changed, especially if you intend to use the [caching
  system](Caching.html).
* `part_data`: a dictionary containing data about the part being analyzed (for
  `update_part_objects`) or with a list of all the `part_data` (for
  `update_score_objects`). In it, you can find the `music21` object of the part, the part
  name, etc. This object should **never** be changed, especially if you intend to use
  the [caching system](Caching.html)
* `cfg`: a [configuration](Configuration.html) object that can be used to access
  the configuration options.
* `parts_features`: a dictionary with the features already computed by the previous calls to `update_part_objects` on this score (or window), e.g. for the previously computed features or for the other parts; these features are not inserted into the final DataFrame.
* `score_features`: a dictionary with the features already computed by the previous
  calls to `update_score_objects` on this score (or window), e.g., for the previously
  computed features; the keys of this dictionary
  are the columns of the DataFrame produced during the extraction.


There are two options in the [configuration](./Config_extraction_example.html) that
allow extending the features computed:
* `basic_modules_addresses` for extending basic features
* `feature_modules_addresses` for extending generic features

By default, their values will be `["musif.extract.basic_modules"]` and
`["musif.extract.features"]`. For instance, the following allow to re-use the stock
features; if you omit the `"musif.extract.basic_modules"`, then the stock features will
no longer be usable:

```yaml
basic_modules_addresses: ["musif.extract.basic_modules", "custom_basic_modules"]
```

## Examples

In the following we will show 3 different examples of custom features. To start,
let's create the `custom_features` directory, where we will store all our files: 
`mkdir custom_features`.

### 1. Custom feature as a package

If you are going to write numerous features, you should likely choose this
method. With it, each feature is implemented as a Python package. This is how
all the `musif` features are implemented.

First, let's create a directory for the package and a `__init__.py` file in it:
We should also create a module named `handler` inside `custom_feature_package`. The
final directory structure looks like this:
```
custom_feature_package
├── handler.py
└── __init__.py
```

`handler.py` will look like this:
```python
def update_part_objects(
    score_data: dict = None,
    parts_data: list = None,
    cfg: object = None,
    parts_features: list = None,
):
    print(
        "We are updating stuffs from module inside a package  given its parent package (part)!"
    )
    parts_features['OurNewFeature'] = 1


def update_score_objects(
    score_data: dict = None,
    parts_data: list = None,
    cfg: object = None,
    parts_features: list = None,
    score_features: dict = None,
):
    print(
        "We are updating stuffs from module inside a package given its parent package (score)!"
    )
    score_features['OurNewFeature'] = 0
```

In the configuration:
```yaml
feature_modules_addresses: 
  - "musif.extract.features"
  - "custom_features"

features:
   - custom_feature_package
```

### 2. Custom feature as a class

If you are writing just a few features, you may find more confortable with only one file,
instead of a whole directory. For this, you can simply create your module
`custom_feature_module.py`:

```python
class custom_feature_class:
    class handler:
        
        def update_part_objects(
            self,
            score_data: dict = None,
            parts_data: list = None,
            cfg: object = None,
            parts_features: list = None,
        ):
            print(
                "We can even update stuffs from an inner class given a module (part)!"
            )

        def update_score_objects(
            self,
            score_data: dict = None,
            parts_data: list = None,
            cfg: object = None,
            parts_features: list = None,
            score_features: dict = None,
        ):
            print(
                "We can even update stuffs from an inner class given a module (score)!"
            )

```

In the configuration file:
```yaml
feature_modules_addresses: 
  - "musif.extract.features"
  - "custom_feature_module"

features:
   - custom_feature_class
```

If the above code looks weird (with the inner static class and classes having lower
initials), you can also opt for a more object-oriented approach:

```python
class FeatureCreator:
    def __init__(self, feature_type, *args, **kwargs):
      self.handler = feature_type(*args, **kwargs)

class MyNewFeature:
  def __init__(*args, **kwargs):
    pass
    
  def update_part_objects(
      self,
      score_data: dict = None,
      parts_data: list = None,
      cfg: object = None,
      parts_features: list = None,
  ):
      print(
          "We can even update stuffs from an inner class given a module (part)!"
      )

  def update_score_objects(
      self,
      score_data: dict = None,
      parts_data: list = None,
      cfg: object = None,
      parts_features: list = None,
      score_features: dict = None,
  ):
      print(
          "We can even update stuffs from an inner class given a module (score)!"
      )


custom_feature_class = FeatureCreator(MyNewFeature, 'other', 'args')
```

### 3. Custom feature as a module

The third option you have actually comes out of the box from the above. You can create a
module inside a package `custom_features/custom_feature_module_in_package.py`:

```python
class handler:
    
    def update_part_objects(
        self,
        score_data: dict = None,
        parts_data: list = None,
        cfg: object = None,
        parts_features: list = None,
    ):
        print(
            "We are updating stuffs from a class inside a module given a package (part)!"
        )
        
    def update_score_objects(
        self,
        score_data: dict = None,
        parts_data: list = None,
        cfg: object = None,
        parts_features: list = None,
        score_features: dict = None,
    ):
        print(
            "We are updating stuffs from a class inside a module given a package (score)!"
        )

```

And then in the configuration file:
```yaml
feature_modules_addresses: 
  - "musif.extract.features"
  - "custom_features"

features:
   - custom_feature_module_in_package
```
