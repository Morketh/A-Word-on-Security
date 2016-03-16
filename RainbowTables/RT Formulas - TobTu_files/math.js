function startHoverVar()
{
	var vars = document.getElementsByTagName('var');

	for (var i in vars)
	{
		if (vars[i].addEventListener)
		{
			vars[i].addEventListener("mouseover", function(){hoverVar(this.innerHTML)}, false);
//			vars[i].addEventListener("mouseout", function(){hoverVar('')}, false);
		}
		else if (vars[i].attachEvent)
		{
			vars[i].attachEvent("onmouseover", hoverVarIE);
//			vars[i].attachEvent("onmouseout", unhoverVarIE);
		}
	}
}

function hoverVarIE(e)
{
	var o;
	if (e.target)
	{
		o = e.target;
	}
	else if (e.srcElement)
	{
		o = e.srcElement;
	}
	if (o && o.nodeType == 3) // defeat Safari bug
		o = o.parentNode;
	hoverVar(o.innerHTML);
}

function unhoverVarIE(e)
{
	hoverVar('');
}

function hoverVar(varName)
{
	var vars = document.getElementsByTagName('var');

	for (var i in vars)
	{
		var cl = vars[i].classList;
		if (cl)
		{
			if (vars[i].innerHTML == varName)
			{
				cl.add('selected');
			}
			else
			{
				cl.remove('selected');
			}
		}
		else if (vars[i].innerHTML == varName)
		{
			addClass(vars[i],'selected');
		}
		else
		{
			removeClass(vars[i],'selected');
		}
	}
}