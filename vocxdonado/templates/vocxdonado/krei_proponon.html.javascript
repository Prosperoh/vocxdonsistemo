{% extends "base.html" %}

{% load static %}

{% block subtitolo %}Krei novan proponon{% endblock subtitolo %}

{% block enhavo %}
<h1>Krei novan proponon</h1>

<script>
	function genInputFields() {
		var quantity =
			document.getElementById("id_nombro_eblaj_elektoj").value;
		var forms = document.getElementById("forms");
		var children = forms.getElementsByTagName("input");
		var currentValues = [];
		for (i = 0; i < children.length; i++) {
            if (children[i].type == 'text') {
                currentValues.push(children[i].value);
                console.log(children[i].value);
            }
		}
		console.log("\n");
		while (forms.firstChild) {
		    forms.removeChild(forms.firstChild);
		}

		for (i = 0; i < quantity; i++) {
            var label = document.createElement("label");
            label.for = "id_elekto_set-" + i + "-enhavo";
            label.innerHTML = "Elekto " + (i+1) + ": ";
			var input = document.createElement("input");
			input.type = "text";
			input.maxlength = 128;
			input.name = "id_elekto_set-" + i + "-enhavo";
			input.id = "id_elekto_set-" + i + "-enhavo";
			if (currentValues[i] != undefined) {
				input.value = currentValues[i];
			}
            var hidden = document.createElement("input");
            hidden.type = "hidden";
            hidden.name = "elekto_set-" + i + "-ligita_propono";
            hidden.id = "id_elekto_set-" + i + "-ligita_propono";
            /*
            var div = document.createElement("div");
            div.id = "elekto".i;
            div.appendChild(label);
            div.appendChild(input);
            div.appendChild(
            */
			forms.appendChild(label);
			forms.appendChild(input);
			forms.appendChild(hidden);
            forms.append(document.createElement("br"));
		};
        // Updating number of total forms
        document.getElementById("elekto_set-TOTAL_FORMS").value = quantity;
	}

    window.onload = genInputFields;
</script>
<form method="post" id="total_form" action="">{% csrf_token %}
	{{ propono_form.as_p }}
	{{ elektoj_formset.management_form }}
    <div id="forms"></div><!-- where the generated forms go -->
	<button type="submit" class="save btn btn-default">Enregistrigi</button>
</form>

{% endblock enhavo %}
