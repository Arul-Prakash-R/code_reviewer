public ActionResult RedirectUser(string returnUrl)
{
    return Redirect(returnUrl); // ?returnUrl=http://evil.com
}
