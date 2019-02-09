import web
        
urls = (
    '/principal', 'application.controllers.personas.index.Index',
    '/', 'application.controllers.personas.principal.Principal',
    '/prod', 'application.controllers.personas.prod.Prod',
    '/insert', 'application.controllers.personas.insert.Insert',
    '/insertp', 'application.controllers.personas.insertp.Insertp',
    '/update/(.*)', 'application.controllers.personas.update.Update',
    '/updatep/(.*)', 'application.controllers.personas.updatep.Updatep',
    '/delete/(.*)', 'application.controllers.personas.delete.Delete',
    '/deletep/(.*)', 'application.controllers.personas.deletep.Deletep',
    '/view/(.*)', 'application.controllers.personas.view.View',
    '/ver/(.*)', 'application.controllers.personas.ver.Ver',
    '/verp/(.*)', 'application.controllers.personas.verp.Verp',
)

if __name__ == "__main__":
    web.config.debug = False
    app = web.application(urls, globals())
    app.run()
